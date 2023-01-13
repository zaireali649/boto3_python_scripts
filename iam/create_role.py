import boto3

iam = boto3.client('iam')

trust_policy = '''{
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
}
'''


response = iam.create_role(
    RoleName='lambda_role_from_py',
    AssumeRolePolicyDocument=trust_policy
)

print(response)