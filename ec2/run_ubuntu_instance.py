
import boto3

def create_apache_ec2(client, MaxCount=1, MinCount=1, KeyName=None, SecurityGroups=["default"], UserData=None):
    region = client.meta.region_name
    
    amis = {"us-east-1":"ami-09e67e426f25ce0d7", "us-west-2":"ami-03d5c68bab01f3496"}
    
    try:
        ami = amis[region]
    except:
        print("Region not supported")
        return None
    
    if(UserData == None):
        UserData='''#!/bin/bash
        apt update -y
        apt upgrade -y
        apt-get install -y apache2
        systemctl start apache2
        systemctl enable apache2'''
    
    try:
        if(KeyName==None):
            client.run_instances(MaxCount=MaxCount,
                         MinCount=MinCount,
                         ImageId=ami,
                         InstanceType="t2.micro",
                         SecurityGroups=SecurityGroups, # name of the security group
                         UserData=UserData)
        
        else:
            client.run_instances(MaxCount=MaxCount,
                             MinCount=MinCount,
                             ImageId=ami,
                             InstanceType="t2.micro",
                             KeyName=KeyName,
                             SecurityGroups=SecurityGroups, # name of the security group
                             UserData=UserData)
        print("Started")
    except Exception as e:
        print("Failed", e)
    
if __name__ == "__main__":
    client = boto3.client('ec2')
    
    create_apache_ec2(client, KeyName="private-ec2", SecurityGroups=["launch-wizard-6"])