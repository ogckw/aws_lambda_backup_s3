from __future__ import print_function

import json
import urllib
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    print (bucket)
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    print (key)
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print (response)
        print ("CONTENT TYPE: " + response['ContentType'])
        s3.put_object(Body=response['Body'].read(), Bucket='lambdabkt-testsave123',Key=key+'123')
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e