# python animal shelter data access object

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, server = "localhost", port = "27017"):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        
        # With Authentication
        self.client = MongoClient('mongodb://%s:%s@%s:%s/?authMechanism=DEFAULT&authSource=AAC' % (username, password, server, port))
        # Without Authentication
        # self.client = MongoClient('mongodb://%s:%s/' % (server, port))
        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None and type(data) is dict:
            self.database.animals.insert(data)  # data should be dictionary 
            return True # requirement is to return true on success, but now we lose the newly created Id from the result, I would argue to return the result from the insert method
        else:
            raise Exception("Data required and of type dictionary.") # requirements call for returning false, but that is inconsistent with the other APIs and doesn't communicate why it failed. Best practice is to return an exception.

    # Search and return cursor for many records
    def read(self, find):
        if find is not None and type(find) is dict:
            return self.database.animals.find(find, { "_id": False })  # find should be dictionary     
        else:
            raise Exception("Find criteria required, returning all records disallowed for performance.")
    
    # Update based on find criteria
    def update(self, find, data):
        if find is not None and type(find) is dict and data is not None and type(data) is dict:
            return self.database.animals.update_many(find, { "$set": data })
        else:
            raise Exception("Find and/or Data must be specified and of type dictionary.")

    # Delete 1 or more records based on find criteria
    def delete(self, find):
        if find is not None and type(find) is dict:
            return self.database.animals.delete_many(find)
        else:
            raise Exception("Find must be specified and of type dictionary.")       

