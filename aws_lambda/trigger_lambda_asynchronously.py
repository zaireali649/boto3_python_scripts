#%%

# =============================================================================
# script for triggering a lambda asynchronously
# =============================================================================

#%%
# import libraries

import boto3

#%%
# define parameters for run

function_name = 'hello_world'

#%%
# prep boto3 for Lambda

client = boto3.client("lambda")

#%%
# invoke function asynchronously

response = client.invoke(FunctionName=function_name,
                         InvocationType='Event' # asynchronous invoke
                         )
