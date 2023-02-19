import boto3

def list_instance_statuses(ec2_client):
    response = ec2_client.describe_instances()
    
    reservations = response["Reservations"]
    
    instanceStatuses = []
    
    for reservation in reservations:
        instances = reservation["Instances"]
        for instance in instances:
            if("Tags" in instance.keys()):
                tags = instance["Tags"]
                tags = { tag['Key']:tag['Value'] for tag in tags} 
                if("Name" in tags.keys()):            
                    instanceStatuses.append(tags['Name'] + ", State: " + instance["State"]["Name"])
                else:
                    instanceStatuses.append("Null: " + instance['InstanceId'] + ", State: " + instance["State"]["Name"])
            else:
                instanceStatuses.append("Null: " + instance['InstanceId'] + ", State: " + instance["State"]["Name"])
    
    return instanceStatuses
            
if __name__ == "__main__":
    ec2 = boto3.client('ec2')
    instanceStatuses = list_instance_statuses(ec2)
    print('\n'.join(instanceStatuses))