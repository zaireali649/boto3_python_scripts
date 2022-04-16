"""
Your module description
"""

import boto3 as AWS

client = AWS.client('sns')

response = client.list_topics()


#%%
for k,v in response.items():
    #print(k, v)
    pass
    
Topics = response['Topics']

print(len(Topics))

for Topic in Topics:
    TopicArn = Topic['TopicArn']
    response = client.publish(
        TopicArn=TopicArn,
        Message='JSONhariston did it!!!!'
        )
    
    
    
    break