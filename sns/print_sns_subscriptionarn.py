"""
Your module description
"""

import boto3 as AWS

client = AWS.client('sns')

response = client.list_subscriptions()

#%%
for k,v in response.items():
    #print(k, v)
    pass
    
#print(type(response))

Subscriptions = response['Subscriptions']

#print(type(Subscriptions))

print(len(Subscriptions))

for Subscription in Subscriptions:
    print(Subscription['SubscriptionArn'])
    
    