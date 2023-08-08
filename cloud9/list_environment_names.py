import boto3

# Create a boto3 client for AWS Systems Manager (SSM) service.
ssm = boto3.client('ssm')

# Get the AWS access key ID and secret access key from AWS Systems Manager Parameter Store.
access_key_id_aws = ssm.get_parameter(Name='access_key_id_aws')['Parameter']['Value']
secret_access_key_aws = ssm.get_parameter(Name='secret_access_key_aws')['Parameter']['Value']

# Create a boto3 client for AWS Cloud9 service using the retrieved credentials.
cloud9 = boto3.client('cloud9',
    aws_access_key_id=access_key_id_aws,
    aws_secret_access_key=secret_access_key_aws,
)

# List Cloud9 environments.
response = cloud9.list_environments()

# Get the IDs of the Cloud9 environments.
environmentIds = response["environmentIds"]

# Describe the Cloud9 environments using the retrieved IDs.
response = cloud9.describe_environments(
    environmentIds=environmentIds
)

# Extract the environments from the response.
environments = response["environments"]

# Print the name of each Cloud9 environment.
for environment in environments:
    print(environment["name"])
