import boto3
import time


cloudwatch_logs = boto3.client('logs')

try:
    response = cloudwatch_logs.put_log_events(
        logGroupName='lg_from_boto3',
        logStreamName='ls_from_boto3',
        logEvents=[
            {
                'timestamp': round(time.time() * 1000),
                'message': 'Message from Boto3'
            },
        ]
    )
    
    print(response)
except cloudwatch_logs.exceptions.ResourceAlreadyExistsException as e:
    print(e)
