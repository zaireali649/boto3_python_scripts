import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.put_item(
    Item={
        'ID':{
          'S': '2ddf7888-2e48-11ed-a261-0242ac120002'  ,
        },
        'AlbumTitle': {
            'S': 'Somewhat Famous',
        },
        'Artist': {
            'S': 'No One You Know',
        },
        'Song': {
            'S': 'Call Me Today',
        },
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='Music',
)
