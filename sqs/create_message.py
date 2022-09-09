import boto3

sqs = boto3.client('sqs')

response = sqs.send_message(
    QueueUrl='https://queue.amazonaws.com/458806987020/gold-queue',
    MessageBody='Message sent from Python <3'
)

print("Message sent")