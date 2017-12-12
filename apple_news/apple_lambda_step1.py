#coding=utf-8
from __future__ import print_function
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import boto3
import requests
from datetime import datetime
from pytz import timezone

print('Loading function')

# aws s3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # crawl url
    url = 'https://tw.appledaily.com/new/realtime'
    header1 = {
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host':'www.appledaily.com.tw',
    'Pragma':'no-cache',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

    # setting time zone
    taipei_time = timezone('Asia/Taipei')

    now = datetime.now(taipei_time)
    print(now)
    fmt = '%Y-%m-%d %H:%M'
    print (now.strftime(fmt))
    nowdate = now.strftime(fmt)

    # start crawler
    res = requests.get(url, headers=header1)
    # put data to s3 trigger next lambda

    s3.put_object(Body=res.text, Bucket='apple2017input', Key=nowdate+'.html')
    print ('end upload')