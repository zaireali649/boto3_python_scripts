import os
import sys
import boto3
import random

sys.path.append('../')

from sqs.sqs_functions import *

sqs = boto3.client('sqs')

QN = "gold-from-function-script"
message = "Hey from custom SQS python functions! Random number: " + str(random.randint(0,300)).zfill(3)

create_queue(sqs, QN)
qurl = get_queue_url(sqs, QN)
create_message(sqs, qurl, message)
messages = get_messages(sqs, qurl)