import boto3

eventbridge = boto3.client("events")

response = eventbridge.list_rules()

rules = response["Rules"]

for rule in rules:
    print(rule["Name"])