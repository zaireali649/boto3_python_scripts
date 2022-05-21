#%%

import boto3

def create_sns_topic(sns_client, Name):
    sns_client.create_topic(Name=Name)
    
#%%

if __name__ == "__main__":
    sns = boto3.client('sns')
    create_sns_topic(sns, 'Idontknow')