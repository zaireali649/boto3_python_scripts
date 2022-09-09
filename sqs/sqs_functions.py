def create_queue(sqs, QueueName):
    response = sqs.create_queue(
        QueueName=QueueName
    )
    
    print('Queue created')
    
    
def get_queue_url(sqs, QueueName):
    response = sqs.get_queue_url(
        QueueName=QueueName
    )
    
    url = response['QueueUrl']
    
    print(url)
    return url

def delete_queue(sqs, QueueUrl):
    response = sqs.delete_queue(
        QueueUrl=QueueUrl
    )
    
    print("Queue Deleted")

def create_message(sqs, QueueUrl, message):
    response = sqs.send_message(
        QueueUrl=QueueUrl,
        MessageBody=message
    )
    
    print("Message sent")

def get_messages(sqs, QueueUrl):
    response = sqs.receive_message(
        QueueUrl=QueueUrl
    )
    
    messages = response['Messages']
    
    out_messages = []
    
    for message in messages:
        data = message['Body']
        print(data)
        out_messages.append(data)
        
    return out_messages

if __name__ == "__main__":
    import boto3
    import random

    sqs = boto3.client('sqs')
    
    QN = "gold-from-function-2"
    message = "Hey from custom SQS python functions! Random number: " + str(random.randint(0,300)).zfill(3)
    
    create_queue(sqs, QN)
    qurl = get_queue_url(sqs, QN)
    create_message(sqs, qurl, message)
    messages = get_messages(sqs, qurl)
    delete_queue(sqs, qurl)