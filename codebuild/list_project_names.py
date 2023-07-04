import boto3

codebuild = boto3.client('codebuild')

response = codebuild.list_projects()

projects = response["projects"]

for project in projects:
    print(project)