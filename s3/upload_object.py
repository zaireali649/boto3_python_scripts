import boto3

s3 = boto3.client('s3')

filename = 'upload_object.py'

with open(filename, 'rb') as data:
    s3.upload_fileobj(data, 'zali-catch-all', filename)
    print("Object Uploaded")