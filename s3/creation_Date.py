import boto3

s3_resource.list_buckets()["Buckets"][0]["Name"]
creation_date=s3_resource.list_buckets()["Buckets"][0]["CreationDate"]
creation_date.strftime("%d%m%y_%H:%M:%s")

print(creation_date)
print( Buckets["Name"])

##NEEDS EDITING
#s3_client = boto3.client('s3')#bucket_name = s3_client.Bucket('bucket-name')
creation_date = s3_client.meta.client.head_bucket(Bucket=bucket_name)['ResponseMetadata']['HTTPHeaders']['date']
print("Bucket creation date:", creation_date)
