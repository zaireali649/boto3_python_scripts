import boto3

s3 = boto3.client('s3')

bucket_name="smontes-catch-all"
key="list_buckets.py" #name of object
response = s3.delete_object(
    Bucket=bucket_name,
    Key=key
)

    #All the documentation but only Bucket and Key is required
   # response = client.delete_object(
    #Bucket='string',
    #Key='string',
    #MFA='string',
    #VersionId='string',
    #RequestPayer='requester',
    #BypassGovernanceRetention=True|False,
    #ExpectedBucketOwner='string'
#)

#Delete multiple objects
#import boto3
#import os
#import glob
#s3 = boto3.client('s3')
#objects=s3.list_objects(Bucket="smontes-catch-all")["Contents"]

#bucket_name="smontes-catch-all"
#key="list_buckets.py" #name of object

#for s3 in objects:
#    s3 = s3.delete_object(
#    Bucket=bucket_name,
#    Key=s3["Key"]
#)