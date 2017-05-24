#coding=utf-8
from __future__ import print_function
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib
import boto3
from bs4 import BeautifulSoup as bs
import StringIO
import operator

print('Loading function')

# aws s3 client
s3 = boto3.client('s3')


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    print(bucket)
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    print(key)
    res = s3.get_object(Bucket=bucket, Key=key)
    print("CONTENT TYPE: " + res['ContentType'])
    # parser html file
    html = res['Body'].read()
    soup = bs(html, "html.parser")
    rank = soup.select('.rtddd.slvl li h2')
    # count category
    dic = {}
    for ele in rank:
        word = ele.text
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    # sort top 5 category
    sorted_x = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_x[0:5])
    # use memory to write file
    output = StringIO.StringIO()
    for ele in sorted_x[0:5]:
        print(ele[0], ele[1])
        content = ele[0] + ' ' + str(ele[1])
        output.write(content + '\n')
    contents = output.getvalue()
    output.close()
    # upload file to s3
    s3.put_object(Body=contents, Bucket='apple2017output', Key= key+'.output')
    print ('end upload')
