import os
import sys
import boto3

sys.path.append('../')

import ec2.list_instance_ids as lii

ec2 = boto3.client('ec2')
lii.list_instance_ids(ec2)