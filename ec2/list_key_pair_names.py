import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_key_pairs()

keypairs = response["KeyPairs"]

for keypair in keypairs:
    print(keypair["KeyName"])
