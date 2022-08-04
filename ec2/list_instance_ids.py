import boto3

def list_instance_ids(ec2_client):
    response = ec2_client.describe_instances()
    
    reservations = response["Reservations"]
    
    for reservation in reservations:
        instances = reservation["Instances"]
        for instance in instances:
            instanceId = instance["InstanceId"]
            
            print(instanceId)
            
if __name__ == "__main__":
    ec2 = boto3.client('ec2')
    list_instance_ids(ec2)