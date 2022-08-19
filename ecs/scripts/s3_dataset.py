import os
import boto3
from botocore import UNSIGNED
from botocore.config import Config

class S3DataSetClient:
    def __init__(self, region, bucket, prefix) -> None:
        self.region = region
        self.bucket = bucket
        self.prefix = prefix
        self.s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

    def get_all_s3_filepaths(self):
        """Get a list of all keys in an S3 bucket."""
        keys = []
        kwargs = {'Bucket': self.bucket, 'Prefix': self.prefix}
        while True:
            resp = self.s3.list_objects_v2(**kwargs)
            for obj in resp['Contents']:
                keys.append(f"{obj['Key']}")
            try:
                kwargs['ContinuationToken'] = resp['NextContinuationToken']
            except KeyError:
                break
        
        return keys
    
    # Total Objects: 175
    # Total Size: 2.9 GiB
    def downloadFile(self, src, dest):
        """Download a single file from the configured bucket"""
        try:
            self.s3.download_file(self.bucket, src, dest)
        except:
            print("Could not download the file")

    def downloadFiles(self, dest="tmp/"):
        """
        objects: list of strings contain object key
        dest: folder path that files are going to be stored (should be ending with '/')
        """
        
        objects = self.get_all_s3_filepaths()

        if not os.path.exists(dest):
            os.mkdir(dest)

        for object in objects:
            name = object.split('/')[-1]
            self.downloadFile(src = object, dest = (dest + name))
        

