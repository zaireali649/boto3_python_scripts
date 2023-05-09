# import the boto3 library
import boto3

# create an AWS Lambda client object
aws_lambda = boto3.client('lambda')

# make a request to the AWS Lambda API to list all available functions
response = aws_lambda.list_functions()

# extract the list of functions from the API response
functions = response["Functions"]

# iterate over the list of functions and print the function name and memory size
for function in functions:
    print(function["FunctionName"], function["MemorySize"])
    
# The code imports the boto3 library, creates a client object for AWS Lambda, makes a request to the AWS Lambda API to list all available functions,
# extracts the list of functions from the API response, iterates over the list of functions, and prints the name and memory size of each function.
