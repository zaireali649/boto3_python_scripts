import boto3

vpc_client = boto3.client('ec2')

response = vpc_client.describe_vpcs()

vpcs = response['Vpcs']

for vpc in vpcs:
    print(vpc['VpcId'])
