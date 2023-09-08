import boto3
import uuid

# Create a CodeCommit client
codecommit = boto3.client('codecommit')

# Create a new CodeCommit repository with the specified name
response = codecommit.create_repository(
    repositoryName='zali-boto3-{}'.format(str(uuid.uuid4()))
)

# Print the response from the repository creation
print(response)
