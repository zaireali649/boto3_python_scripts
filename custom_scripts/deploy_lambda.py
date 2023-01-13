import os
import sys
import boto3
import string
import random

sys.path.append('../')

import aws_lambda.create_function as lcf

aws_lambda_client = boto3.client('lambda')

res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=7))
                             
functionName = 'python_boto3_lambda_' + res



response = lcf.create_function(aws_lambda_client, 
    'arn:aws:iam::458806987020:role/service-role/luit_red_jan_2023_lambda-role-fo8jlfny', 
    'zali-catch-all', 
    'lambda_function.zip',
    functionName = functionName
    )

print(response)