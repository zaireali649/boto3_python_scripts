# Import the 'boto3' library, which provides an interface to interact with Amazon Web Services (AWS)
import boto3

# Create an 'ec2' client using the 'boto3.client()' method, allowing interaction with AWS Elastic Compute Cloud (EC2) service
vpc = boto3.client('ec2')

# Use the 'describe_vpcs()' method of the 'vpc' client to retrieve information about Virtual Private Clouds (VPCs)
response = vpc.describe_vpcs()

# Extract the list of VPCs from the 'response' dictionary
vpcs = response["Vpcs"]

# Iterate through each VPC in the 'vpcs' list
for vpc in vpcs:
    # Print the VPC ID and CIDR block (IP address range) associated with each VPC
    print(vpc["VpcId"], vpc["CidrBlock"])
