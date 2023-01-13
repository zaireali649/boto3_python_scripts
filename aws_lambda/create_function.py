import boto3

def create_function(client, roleARN, s3_bucket, s3_key, functionName='python_boto3_lambda', runtime='python3.8', handler='lambda_function.lambda_handler'):
    response = client.create_function(
        FunctionName=functionName,
        Runtime=runtime,
        Handler=handler,
        Role=roleARN,
        Code={
            'S3Bucket': s3_bucket,
            'S3Key': s3_key,
        }
    )
    
    return response



if(__name__ == "__main__"):
    aws_lambda = boto3.client('lambda')
    
    response = create_function(aws_lambda, 'arn:aws:iam::458806987020:role/service-role/luit_red_jan_2023_lambda-role-fo8jlfny', 'zali-catch-all', 'lambda_function.zip')
    
    print(response)