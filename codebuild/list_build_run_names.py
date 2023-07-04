import boto3

codebuild = boto3.client('codebuild')

response = codebuild.list_builds_for_project(
    projectName='black-may-2023'
)

names = response["ids"]

for name in names:
    print(name)