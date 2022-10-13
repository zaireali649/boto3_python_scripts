import boto3

vpc = boto3.client('ec2')

response = vpc.describe_subnets()

subnets = response['Subnets']

for subnet in subnets:
    print(subnet['SubnetId'])