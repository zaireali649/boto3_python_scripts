import boto3

vpc = boto3.client("ec2")

response = vpc.delete_vpc(
    VpcId = 'vpc-03048ed7af91f8a11'
    
    )

#vpc = response["VPC"]
#for subnet in subnets:
    #print(subnet["SubnetId"])
    
print("VPC deleted")