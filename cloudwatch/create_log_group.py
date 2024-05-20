import boto3

cloudwatch_logs = boto3.client('logs')

try:
    response = cloudwatch_logs.create_log_group(
        logGroupName='lg_from_boto3'
    )
    
    print(response)
except cloudwatch_logs.exceptions.ResourceAlreadyExistsException as e:
    print(e)
