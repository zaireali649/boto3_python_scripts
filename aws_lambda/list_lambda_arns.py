import boto3

aws_lambda = boto3.client('lambda')

response = aws_lambda.list_functions()

functions = response['Functions']

for function in functions:
    print(function['FunctionArn'])
