from __future__ import print_function
import boto3
import os
import sys
import uuid
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)    
     
s3 = boto3.resource('s3')
 
def hello(event, context):
    print('I can log with a Python print statement.')

    logger.info('I can also log with the Python logging library.')

    for record in event['Records']:
        print(record)
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key'] 
        print('the bucket name: '+ bucket + ', the key name: ' + key)
        obj = s3.Object(bucket, key)
        blah = obj.get()['Body'].read().decode('utf-8')
        print(blah)
        return blah
