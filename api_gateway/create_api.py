# import libraries

import boto3

#%%
apigateway = boto3.client('apigatewayv2')

response = apigateway.create_api(
    Name='silver-sept-2023-api',
    ProtocolType='HTTP',
    Target='arn:aws:lambda:us-east-1:458806987020:function:silver-sept-2023-lambda'
)

print(response)