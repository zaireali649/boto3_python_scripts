import boto3

cloudwatch_logs = boto3.client('logs')

logGroups = []
next_token = None

# Use a while loop to handle pagination
while True:
    if next_token:
        response = cloudwatch_logs.describe_log_groups(nextToken=next_token)
    else:
        response = cloudwatch_logs.describe_log_groups()
    
    logGroups.extend(response['logGroups'])
    
    # Check if there is a nextToken to continue pagination
    next_token = response.get('nextToken')
    if not next_token:
        break

print(len(logGroups))

for logGroup in logGroups:
    print(logGroup['logGroupName'])
