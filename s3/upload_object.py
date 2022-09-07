import boto3

s3 = boto3.client('s3')

filename = 'upload_object.py'
bucket_name="zali-catch-all"

with open(filename, 'rb') as data:
    s3.upload_fileobj(data, bucket_name, filename)
    print("Object Uploaded")