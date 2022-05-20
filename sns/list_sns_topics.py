#%%

import boto3

def list_sns_topics(sns_client):
    Topics =  sns_client.list_topics()['Topics']
    return [Topic['TopicArn'] for Topic in Topics]
    
#%%

if __name__ == "__main__":
    sns = boto3.client('sns')
    topics = list_sns_topics(sns)