#%%

import boto3

client = boto3.client("s3")

#%%

s3 = boto3.resource('s3')
bucket = s3.Bucket("zali-bucket-test-boto3")

bucket.create()

bucket.delete()