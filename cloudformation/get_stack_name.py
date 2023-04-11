import boto3

cloudformation = boto3.client('cloudformation')

response = cloudformation.describe_stacks()

stacks = response['Stacks']

for stack in stacks:
    print(stack['StackName'])
