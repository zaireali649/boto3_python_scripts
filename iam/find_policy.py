import boto3

iam = boto3.client('iam')

policy_name = 'lambda_sns_s3'

response = iam.list_policies()

policies = response['Policies']

for policy in policies:
    if(policy_name in policy['PolicyName']):
        print(policy['PolicyName'], policy['Arn'])