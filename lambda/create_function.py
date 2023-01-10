import boto3

aws_lambda = boto3.client('lambda')

response = aws_lambda.create_function(
    FunctionName='black_boto3_lambda',
    Runtime='python3.8',
    Handler='lambda_function.lambda_handler',
    Role='arn:aws:iam::458806987020:role/service-role/luit_red_jan_2023_lambda-role-fo8jlfny',
    Code={
        'S3Bucket': 'zali-catch-all',
        'S3Key': 'lambda_function.zip',
    }
)

print(response)