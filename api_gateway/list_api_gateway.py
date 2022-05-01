#%%

# =============================================================================
# script for listing apis
# =============================================================================

#%%
# import libraries

import boto3

#%%
# prep boto3 for Lambda

client = boto3.client('apigateway')

#%%
# get apis

response = client.get_rest_apis()

#%%


items = response['items']

for item in items:
    print(item['name'])