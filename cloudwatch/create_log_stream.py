import boto3

cloudwatch_logs = boto3.client('logs')

try:
    response = cloudwatch_logs.create_log_stream(
        logGroupName='lg_from_boto3',
        logStreamName='ls_from_boto3'
    )
    
    print(response)
except cloudwatch_logs.exceptions.ResourceAlreadyExistsException as e:
    print(e)
