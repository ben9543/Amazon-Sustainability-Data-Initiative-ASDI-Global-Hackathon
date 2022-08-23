# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
import boto3
from botocore.exceptions import ClientError
import logging
import os

BUCKET_NAME = "asdi-hackathon-data"
REGION = "us-west-1"

# Using default profile (attached role)
session = boto3.Session(region_name = REGION)
client = session.client('s3')

def upload_file(file_name, object_name):
    try:
        response = client.upload_file(file_name, BUCKET_NAME, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_json_files(folder_path):
    pass