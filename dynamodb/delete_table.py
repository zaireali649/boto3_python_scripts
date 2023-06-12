import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.delete_table(TableName='hells_kitchen')

print(response)