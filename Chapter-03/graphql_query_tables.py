from azure.identity import InteractiveBrowserCredential
import requests
import json

# Acquire a token
# DO NOT USE IN PRODUCTION.
# Below code to acquire token is for development purpose only to test the GraphQL endpoint
# For production, always register an application in a Microsoft Entra ID tenant and use the appropriate client_id and scopes
# https://learn.microsoft.com/en-us/fabric/data-engineering/connect-apps-api-graphql#create-a-microsoft-entra-app

app = InteractiveBrowserCredential()
scp = 'https://analysis.windows.net/powerbi/api/user_impersonation'


### For production use 

# CLIENT_ID = "<client_id>"  # Your Application ID
# TENANT_ID = "<tenant_id>"  # Your Tenant ID
# AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
# app = PublicClientApplication(CLIENT_ID, authority=AUTHORITY)
# scp = 'https://analysis.windows.net/powerbi/api/.default'


result = app.get_token(scp)

if not result.token:
    print('Error:', "Could not get access token")

# Prepare headers
headers = {
    'Authorization': f'Bearer {result.token}',
    'Content-Type': 'application/json'
}

endpoint = 'https://cd40d6ac-6f7a-4999-915d-7fcfde88b2c8.zcd.msitgraphql.fabric.microsoft.com/v1/workspaces/cd40d6ac-6f7a-4999-915d-7fcfde88b2c8/graphqlapis/9755e57c-a202-47cd-bf91-80fce2d3b31b/graphql'
query = """
    query{
    customers {
       items {
          Title,
          CustomerID,
          Phone,   
       }
    },
    addresses {
        endCursor,    
        hasNextPage,    
       items {
          City         
       }
    }
}
"""

variables = {
    
  }
  

# Issue GraphQL request
try:
    response = requests.post(endpoint, json={'query': query, 'variables': variables}, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(json.dumps(data, indent=4))
except Exception as error:
    print(f"Query failed with error: {error}")
