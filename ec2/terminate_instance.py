import boto3

ec2 = boto3.client('ec2')

instanceId = ''

response = ec2.terminate_instances(InstanceIds=[instanceId])
print(response)