from run_ubuntu_instance import *

client = boto3.client('ec2')

create_apache_ec2(client, KeyName="private-ec2", SecurityGroups=["launch-wizard-6"])