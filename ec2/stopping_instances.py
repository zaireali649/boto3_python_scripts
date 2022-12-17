import boto3

ec2 = boto3.client('ec2')

dev_tag = { "Key":"Environment", "Value":"Dev"}

response = ec2.describe_instances()

reservations = response['Reservations']

for reservation in reservations:
    instances = reservation['Instances']

    for instance in instances:
        if (dev_tag in instance['Tags'] and 'running' in instance['State']['Name']):
            print(instance['InstanceId'])
            ec2.stop_instances(InstanceIds=[instance['InstanceId']])