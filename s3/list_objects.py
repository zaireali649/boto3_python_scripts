import boto3

s3 = boto3.client('s3')

bucket_name="zali-catch-all"

response = s3.list_objects(
    Bucket=bucket_name
)

contents = response['Contents']

for content in contents:
    print(content['Key'])