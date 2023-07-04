import boto3

codebuild = boto3.client('codebuild')

response = codebuild.list_projects()

projects = response["projects"]

for project in projects:
    print(project)
    response = codebuild.list_builds_for_project(
        projectName=project
    )
    
    names = response["ids"]
    
    for name in names:
        print(name)
        response = codebuild.batch_get_builds(
            ids=[
                name,
            ]
        )
        
        builds = response["builds"]
        
        for build in builds:
            print(build["id"], build["arn"])