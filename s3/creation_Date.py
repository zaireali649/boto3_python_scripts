import boto3

#s3_client = boto3.client('s3')#bucket_name = s3_client.Bucket('bucket-name')
creation_date = s3_client.meta.client.head_bucket(Bucket=bucket_name)['ResponseMetadata']['HTTPHeaders']['date']
print("Bucket creation date:", creation_date)
