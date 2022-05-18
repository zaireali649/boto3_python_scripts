#%%

# create a S3 Bucket

import boto3

client = boto3.client("s3")

#%%

client.create_bucket(Bucket="zali-bucket-test-boto3") 
