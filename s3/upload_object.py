import boto3
import os
import glob


s3 = boto3.client('s3')

filename = 'list_buckets.py'
bucket_name="smontes-catch-all"

with open(filename, 'rb') as data:
    s3.upload_fileobj(data, bucket_name, filename)
    print("Object Uploaded")
  
#how to upload multiple files  
#cwd=os.getcwd()
#cwd=cwd+"/upload"
#files=glob.glob(cwd+"*.png") #all png files
#files
#for file in files:
 #   s3 =boto3.client('s3')
 #   s3.upload_fileobj(
 #      filename=file,
 #      bucket_name="smontes-catch-all",
 #      Key=file.split("/")[-1])
