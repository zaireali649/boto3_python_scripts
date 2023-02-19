import boto3

def list_instance_names(ec2_client):
    response = ec2_client.describe_instances()
    
    reservations = response["Reservations"]
    
    instanceNames = []
    
    for reservation in reservations:
        instances = reservation["Instances"]
        for instance in instances:
            if("Tags" in instance.keys()):
                tags = instance["Tags"]
                tags = { tag['Key']:tag['Value'] for tag in tags} 
                if("Name" in tags.keys()):            
                    instanceNames.append(tags['Name'])
                else:
                    instanceNames.append("Null: " + instance['InstanceId'])
            else:
                instanceNames.append("Null: " + instance['InstanceId'])
    
    return instanceNames
            
if __name__ == "__main__":
    ec2 = boto3.client('ec2')
    instanceNames = list_instance_names(ec2)
    print('\n'.join(instanceNames))