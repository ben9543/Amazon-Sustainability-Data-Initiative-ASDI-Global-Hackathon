# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import logging
import os
import glob

load_dotenv()

BUCKET_NAME = "asdi-hackathon-data"
REGION = "us-west-1"

# Using default profile (attached role)
'''
session = boto3.Session(region_name = REGION)
client = session.client('s3')
'''

# 
client = boto3.client(
    's3',
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_KEY"),
    region_name=REGION
)

def upload_file(file_name, object_name):
    try:
        response = client.upload_file(file_name, BUCKET_NAME, object_name)
        if(response):print("Success")
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_json_files(folder_path):

    file_names = map(os.path.basename, glob.glob(folder_path))
    for file_name in file_names:
        src = f"json/{file_name}"
        dest = f"json/{file_name}"
        upload_file(src, dest)


upload_json_files("./json/*")