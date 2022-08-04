import os
import sys
import boto3

sys.path.append('../')

import ec2.list_instance_ids as lii
import sns.publish_sns_topic as pst

ec2 = boto3.client('ec2')
instanceIds = lii.list_instance_ids(ec2)

sns = boto3.client('sns')

for instanceId in instanceIds:
    pst.sns_publish_topic(sns, 'arn:aws:sns:us-east-1:458806987020:Idontknow', instanceId)