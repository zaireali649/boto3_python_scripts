import boto3
client=boto3.resource("s3")

bucket_list=list(client.buckets.all())
len(bucket_list)

for bucket in client.buckets.all():
    print(bucket.name)
