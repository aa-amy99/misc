import logging

import boto3
from botocore.exceptions import ClientError
import pandas as pd
import io

#upload file to S3
def upload_file_s3(file_name, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

bucket_name  = 'ner-data'
local_file_name = 'data/tweets.csv'
aws_file_name = 'input-data/tweets.csv'
# Upload file to specific location
#upload_file_s3(local_file_name, bucket_name, aws_file_name)


def download_file_s3( bucket, object_name):

    s3_client = boto3.client('s3')
    try:
        s3_response_object = s3_client.get_object(Bucket=bucket, Key=object_name)
        #object_content = s3_response_object['Body'].read()
        df = pd.read_csv(io.BytesIO(s3_response_object['Body'].read()), encoding='utf8')
        print(s3_response_object )
        return df
    except ClientError as e:
        logging.error(e)


df = download_file_s3(bucket_name, aws_file_name)
print(df.head())

'''
import boto3
import pandas as pd
import io
REGION = 'us-east-1'
ACCESS_KEY_ID = 'paste_here_your_key_id'
SECRET_ACCESS_KEY = 'paste_here_your_secret_access_key'
BUCKET_NAME = 'vperezb'
KEY = 'path/in/s3/namefile.txt' # file path in S3 
s3c = boto3.client(
        's3', 
        region_name = REGION,
        aws_access_key_id = ACCESS_KEY_ID,
        aws_secret_access_key = SECRET_ACCESS_KEY
    )
obj = s3c.get_object(Bucket= BUCKET_NAME , Key = KEY)
df = pd.read_csv(io.BytesIO(obj['Body'].read()), encoding='utf8')
df
'''



