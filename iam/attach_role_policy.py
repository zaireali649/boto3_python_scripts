import boto3

iam = boto3.client('iam')




response = iam.attach_role_policy(
    RoleName='lambda_role_from_py', PolicyArn='arn:aws:iam::458806987020:policy/lambda_sns_s3')
    
print(response)