#coding=utf-8
from __future__ import print_function
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba
import json
import urllib
import boto3
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
from pytz import timezone
import shutil


print('Loading function')

# aws client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # crawl url
    url = 'http://beauty.zones.gamebase.com.tw/wall_rank/day'
    header1 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
              'Cache-Control': 'no-cache',
              'Connection': 'keep-alive',
              'Host': 'beauty.zones.gamebase.com.tw',
              'Pragma': 'no-cache',
              'Referer': 'http://beauty.zones.gamebase.com.tw/wall',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
              Chrome/56.0.2924.87 Safari/537.36'
              }

    # setting time zone
    taipei_time = timezone('Asia/Taipei')

    now = datetime.now(taipei_time)
    print(now)
    fmt = '%Y-%m-%d'
    print (now.strftime(fmt))
    nowdate = now.strftime(fmt)

    # start crawler
    res = requests.get(url, headers=header1)
    soup = bs(res.text, "html.parser")
    rank = soup.select('#rank_list .clearfix h4')
    image = soup.select('#rank_list .clearfix img')

    header2 = {'Accept': 'image/webp,image/*,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch',
               'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
               'Cache-Control': 'no-cache',
               'Connection': 'keep-alive',
               'Host': 'i.gbc.tw',
               'Pragma': 'no-cache',
               'Referer': 'http://beauty.zones.gamebase.com.tw/wall_rank/day',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
               }

    # start crawler images
    for ele in zip(rank, image):
        print(ele[0].text, ele[1]['src'])
        fname = ele[0].text
        img_url = ele[1]['src']
        extention = img_url.split('.')[-1]
        print (extention)
        pic = requests.get(img_url, headers=header2, stream=True)
        print ('start')
        filepath = '{}.{}'.format(fname, extention)
        #filepath = unicode(filepath, 'utf8')
        if pic.status_code == 200:
            pic.raw.decode_content = True
            s3.put_object(Body=pic.raw.read(), Bucket='beautywall001', Key=nowdate + '/' + filepath)
        # with open(filepath, 'wb') as f:
        #     print('write file')
        #     pic.raw.decode_content = True
        #     shutil.copyfileobj(pic.raw, f)
    print ('end upload')




