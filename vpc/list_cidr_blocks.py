# Import the boto3 library for AWS interaction
import boto3

# Create an EC2 client object
vpc = boto3.client('ec2')

# Use the client to describe VPCs and store the response
response = vpc.describe_vpcs()

# Extract the VPCs information from the response
vpcs = response['Vpcs']

# Iterate through each VPC and print its ID and CIDR block
for vpc in vpcs:
    print(vpc["VpcId"], ':', vpc["CidrBlock"])
