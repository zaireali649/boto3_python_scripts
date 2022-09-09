import boto3

sqs = boto3.client('sqs')

response = sqs.get_queue_url(
    QueueName='gold-queue'
)

url = response['QueueUrl']

print(url)