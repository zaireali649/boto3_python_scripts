import boto3 as AWS

client = AWS.client('sns')

response = client.list_subscriptions()

#%%

Subscriptions = response['Subscriptions']

print(len(Subscriptions))

for Subscription in Subscriptions:
    print(Subscription['SubscriptionArn'])
    
    