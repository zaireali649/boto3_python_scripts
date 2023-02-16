#%%

import boto3

def create_apache_ec2(client):
    try:
        client.run_instances(MaxCount=1,
                         MinCount=1,
                         ImageId="ami-0f1a5f5ada0e7da53",         # us-west-2 ami as of 2/16/23
                         InstanceType="t2.micro",
                         KeyName="private-ec2",
                         SecurityGroups=["launch-wizard-6"],
                         UserData=boot_apache2_script)
        print("Started")
    except:
        print("Failed")
    

#%%
client = boto3.client('ec2')
#%%

boot_apache2_script='''#!/bin/bash
apt update -y
apt upgrade -y
apt-get install -y apache2
systemctl start apache2
systemctl enable apache2'''


#%%

create_apache_ec2(client)