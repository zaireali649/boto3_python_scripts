import boto3

codebuild = boto3.client('codebuild')

response = codebuild.batch_get_builds(
    ids=[
        'black-may-2023:d5b4bb81-c554-470d-bd48-0fca6b8ae5b2',
    ]
)

builds = response["builds"]

for build in builds:
    print(build["id"], build["arn"])