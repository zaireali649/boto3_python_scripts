import boto3

sqs = boto3.client('sqs')

response = sqs.receive_message(
    QueueUrl='https://queue.amazonaws.com/458806987020/gold-queue'
)

messages = response['Messages']

for message in messages:
    data = message['Body']
    print(data)