import boto3

ec2 = boto3.client('ec2')

response = ec2.terminate_instances(InstanceIds=['i-008b3242f0d8b4d9a'])

print(response)