import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.list_tables()

tableNames = response["TableNames"]

for tableName in tableNames:
    print(tableName)
