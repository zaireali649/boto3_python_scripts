import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.scan(TableName='movies')

items = response["Items"]

for item in items:
    print(item)
    for k, v in item.items():
        print(k, list(v.values())[0])