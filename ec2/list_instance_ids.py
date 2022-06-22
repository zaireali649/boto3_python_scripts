import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

reservations = response["Reservations"]

for reservation in reservations:
    instances = reservation["Instances"]
    for instance in instances:
        instanceId = instance["InstanceId"]
        if("i-0c20739c3c11da9fb" != instanceId):
            print(instanceId)