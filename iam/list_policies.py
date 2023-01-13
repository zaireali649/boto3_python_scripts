import boto3

iam = boto3.client('iam')

response = iam.list_policies()

policies = response['Policies']

for policy in policies:
    print(policy['PolicyName'], policy['Arn'])