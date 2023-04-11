import boto3
import uuid # random string library

cloud9 = boto3.client('cloud9')

response = cloud9.create_environment_ec2(
    name=str(uuid.uuid4()),
    instanceType='t2.micro',
    imageId='amazonlinux-2-x86_64')

print(response)