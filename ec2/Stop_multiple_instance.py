import boto3

ec2 = boto3.resource("ec2")

# need the Instance IDs
ec2.Instance('i-0cf014d542a12605a').stop()
ec2.Instance('i-0a680b1f706dd0963').stop()
ec2.Instance('i-083f54d5b7fb83a4f').stop()

