import boto3

sqs = boto3.client('sqs')

response = sqs.delete_queue(
    QueueUrl='https://queue.amazonaws.com/458806987020/gold-queue'
)

print("Queue Deleted")