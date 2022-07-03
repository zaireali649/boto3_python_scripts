import boto3

vpc = boto3.client('ec2')

response = vpc.describe_vpcs()

vpcs = response['Vpcs']

for vpc in vpcs:
    print(vpc['VpcId'])