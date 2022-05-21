#%%

import boto3

def sns_subscribe_email(sns_client, TopicArn, email_address):
    sns_client.subscribe(TopicArn=TopicArn, Protocol='email', Endpoint=email_address)
    
    
#%%

if __name__ == "__main__":
    sns = boto3.client('sns')
    sns_subscribe_email(sns, 'arn:aws:sns:us-east-1:458806987020:Idontknow', 'zaire.ali@levelupintech.com')