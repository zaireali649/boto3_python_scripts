import boto3

ec2 = boto3.resource("ec2")

ec2.create_instances(ImageId='ami-06e46074ae430fba6',
    InstanceType='t2.micro',
    MaxCount=3,
    MinCount=3)
    
print("EC2 instances created")
    
# 3 instances will be created

