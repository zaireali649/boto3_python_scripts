######## Create a Sample Lambda Function URL and the necessary dependencies ########

import boto3

#%%
### Create Hello Lambda .py ###

lambda_code = ''' 
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
'''

f = open("lambda_function.py", "w")
f.write(lambda_code)
f.close()

#%%
### Create handler .zip ###

from zipfile import ZipFile

fZip = ZipFile('lambda-handler.zip', 'w')
fZip.write('lambda_function.py')
fZip.close()


#%%
### Create Trust Policy for IAM Role

import json

trust_policy = json.dumps({
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
    "Action": "sts:AssumeRole"
    }
  ]
})


#%%
### Create IAM Role

client_iam = boto3.client('iam')

response_create_role = client_iam.create_role(
    RoleName='lambda-role-boto3',
    AssumeRolePolicyDocument=trust_policy
)

role_arn = response_create_role['Role']['Arn']
#%%
### Create Lambda Function

client_lambda = boto3.client('lambda')

f = open('lambda-handler.zip', 'rb')
lambda_handler_zip = f.read()
f.close()

response_create_function = client_lambda.create_function(
        FunctionName='test_Lambda_Function_URLs_boto3',
        Runtime= 'python3.9',
        Role=role_arn,
        Code=dict(ZipFile=lambda_handler_zip),
        Handler='lambda_function.lambda_handler'
    )

#%%
### Add Public Access Permission

client_lambda = boto3.client('lambda')

response_add_permission = client_lambda.add_permission(
    FunctionName='test_Lambda_Function_URLs_boto3',
    StatementId='FunctionURLAllowPublicAccess',
    Action='lambda:InvokeFunctionUrl',
    Principal='*',
    FunctionUrlAuthType='NONE'    
    )

#%%
### Create Lambda Function URL

client_lambda = boto3.client('lambda')

response_create_function_url_config = client_lambda.create_function_url_config(
    FunctionName='test_Lambda_Function_URLs_boto3',
    AuthType='NONE'
    )

function_URL = response_create_function_url_config['FunctionUrl']
print(function_URL)

import requests
response_requests = requests.get(function_URL)
print(response_requests.text)

