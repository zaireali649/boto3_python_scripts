#%%

# delete a S3 Bucket

import boto3

s3 = boto3.client('s3')

#%%

s3.delete_bucket(Bucket='zali-bucket-test-boto3')
