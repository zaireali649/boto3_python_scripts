import boto3

def sns_publish_topic(sns_client, TopicArn, Message):
    sns_client.publish(TopicArn=TopicArn, Message=Message)
    print("Sent Message:", Message)

#%%

if __name__ == "__main__":
    sns = boto3.client('sns')
    sns_publish_topic(sns, 'arn:aws:sns:us-east-1:458806987020:Idontknow', 'JSONhariston did it!!!!')