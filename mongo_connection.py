from pymongo import MongoClient

uri = "mongodb://way:findr@54.194.175.227:27017/wayfindr?authMechanism=SCRAM-SHA-1"
client = MongoClient(uri)

db = client.wayfindr
collection = db.test
# document = {"name": "Colin"}
collection.update_one({'Name': "colin"},
                      {"$set": {"Age": "20", 'School': "TCD"}}, upsert=True)


# Change Streams in MongoDB
cursor = db.inventory.watch(full_document='updateLookup')
document = next(cursor)