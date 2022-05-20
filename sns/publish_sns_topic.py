import boto3 as AWS

client = AWS.client('sns')

response = client.list_topics()

#%%
    
Topics = response['Topics']

print(len(Topics))

for Topic in Topics:
    TopicArn = Topic['TopicArn']
    response = client.publish(
        TopicArn=TopicArn,
        Message='JSONhariston did it!!!!'
        )
    
    
    
    break