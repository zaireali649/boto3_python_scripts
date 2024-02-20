import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_volumes()

volumes = response["Volumes"]

for volume in volumes:
    print(volume["VolumeId"])