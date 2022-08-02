import boto3

iam = boto3.client('iam')

response = iam.list_roles()

roles = response['Roles']

for role in roles:
    print(role['RoleName'])