import boto3  # Import the Boto3 library to interact with AWS services

ec2 = boto3.client('ec2')  # Create an EC2 client using Boto3

response = ec2.describe_instances()  # Call the describe_instances method to get information about EC2 instances

reservations = response["Reservations"]  # Extract the reservations from the response

for reservation in reservations:  # Iterate over each reservation
    instances = reservation["Instances"]  # Extract the instances from the reservation
    for instance in instances:  # Iterate over each instance in the reservation
        # Print the instance ID and the availability zone of the instance
        print(instance["InstanceId"], instance["Placement"]["AvailabilityZone"])
