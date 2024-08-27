import boto3  # Import the boto3 library to interact with AWS services

# Create a CloudFront client using boto3
cloudfront = boto3.client('cloudfront')

# List all CloudFront distributions
response = cloudfront.list_distributions()

# Extract the DistributionList from the response
distributionList = response["DistributionList"]

# Get the list of distribution items
items = distributionList["Items"]

# Loop through each distribution item and print its Id
for item in items:
    print(item["Id"])
