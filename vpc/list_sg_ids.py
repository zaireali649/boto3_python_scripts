import boto3

vpc = boto3.client('ec2')

response = vpc.describe_security_groups()

securitygroups = response['SecurityGroups']

for securitygroup in securitygroups:
    print(securitygroup['GroupId'])