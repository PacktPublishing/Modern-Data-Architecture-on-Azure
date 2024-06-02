import os
from dotenv import load_dotenv

load_dotenv()

settings = {
    'host': os.environ.get('ACCOUNT_HOST', os.getenv('ACCOUNT_HOST')),
    'master_key': os.environ.get('ACCOUNT_KEY', os.getenv('ACCOUNT_KEY')),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),

    'tenant_id': os.environ.get('tenant_id'),
    'client_id': os.environ.get('client_id'),
    'client_secret': os.environ.get('client_secret'),


}