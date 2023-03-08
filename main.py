### Import MongoClient instance from pymongo module
from pymongo import MongoClient


def print_hi(name):
    ### Initalize A Client To Connect To MongoDB
    ### Either format is acceptable:
    # client = MongoClient("localhost", 27017)
    client = MongoClient("mongodb://localhost:27017/")
    print('client:\n', client)
    ###############################################################################################################################################################
    ### Connect to specific Database
    #
    # get list of databases
    print("databases =",
          client.list_database_names())  # out: databases = ['admin', 'config', 'local', 'my_store', 'test_db']

    # both of them ok
    # db = client.my_store
    db = client["my_store"]
    print(
        db);  # out: Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'my_store')

    ###############################################################################################################################################################
    ### Access a specific collection within the database
    print('collections:', db.list_collection_names())  # out:collections: ['users']
    users_collection = db.users  # or  db["users"]
    print(users_collection)

    ####################################################################################################################
    ### C - Create
    # Go over how to create new entries in your Mongo Database
    # below code is messy
    users_collection.insert_one({"name": "Sam smith", "age": 23})

    # so suggested to create dictionary first then insert
    new_user = {
        "name": "Kean",
        "age": 99
    }
    users_collection.insert_one(new_user)
    ####################################################################################################################
    ### R - Read
    # Go over how to read in entries that are in your Mongo Database
    found = users_collection.find_one({"name": "Kean", "age": 99})
    print(found)
    # or
    found = users_collection.find_one(new_user)
    print(found)

    found = users_collection.find_one({"name": "Kean", "age": 9999})
    print(found)  # out: None

    ### U - Update
    # Go over how to update existing entries that are in your Mongo Database
    users_collection.update_one({"name": "Sam smith"}, {"$set": {"name": "Will Smith", "age": 53}})

    ### D - Delete
    # Go over how to delete entries that are in your Mongo Database
    users_collection.delete_one({"name":"Will Smith"})
    #delete all
    users_collection.delete_many({})

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
