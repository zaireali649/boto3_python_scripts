import boto3

ec2 = boto3.client('ec2')

instanceIds = ['']

response = ec2.terminate_instances(InstanceIds=instanceIds)

print(response)