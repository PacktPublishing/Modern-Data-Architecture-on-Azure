from azure.identity import ClientSecretCredential
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
from azure.identity import DefaultAzureCredential

from runUtil import  get_sales_order, get_sales_order_v2, HOST


ENDPOINT = HOST#os.environ["COSMOS_ENDPOINT"]



def get_container(DATABASE_ID,CONTAINER_ID):

    credential = DefaultAzureCredential()
    client = cosmos_client.CosmosClient(ENDPOINT, credential)

    db = client.get_database_client(DATABASE_ID)
    print('Database with id \'{0}\' was found'.format(DATABASE_ID))
    container=db.get_container_client(CONTAINER_ID)
    # print(str(container))
    return container

def read_items(container):
    print('\nReading all items in a container\n')

    # NOTE: Use MaxItemCount on Options to control how many items come back per trip to the server
    #       Important to handle throttles whenever you are doing operations such as this that might
    #       result in a 429 (throttled request)
    item_list = list(container.read_all_items(max_item_count=10))

    print('Found {0} items'.format(item_list.__len__()))

    for doc in item_list:
        print('Item Id: {0}'.format(doc.get('id')))
    return item_list
def create_items(container):
    print('\nCreating Items\n')

    # Create a SalesOrder object. This object has nested properties and various types including numbers, DateTimes and strings.
    # This can be saved as JSON as is without converting into rows/columns.
    sales_order = get_sales_order("SalesOrder1")
    container.create_item(body=sales_order)

    # As your app evolves, let's say your object has a new schema. You can insert SalesOrderV2 objects without any
    # changes to the database tier.
    sales_order2 = get_sales_order_v2("SalesOrder2")
    container.create_item(body=sales_order2)

# https://learn.microsoft.com/en-us/azure/cosmos-db/synapse-link-use-cases
if __name__ == "__main__":
    DATABASE_ID="ToDoList"
    CONTAINER_ID="Items"
    container=get_container(DATABASE_ID,CONTAINER_ID)
    # create_items(container)
    item_list=read_items(container)
    for doc in item_list:
        print('Item : {0}'.format(doc))