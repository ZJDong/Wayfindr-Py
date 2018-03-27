from pymongo import MongoClient

client1 = MongoClient('mongodb://54.229.58.205:27017')
db1 = client1.wayfindr
client2 = MongoClient('mongodb://52.31.97.5:27017')
db2 = client2.wayfindr
# collection = db.Noise_Data

# Change Streams in MongoDB
while(1):
    cursor = db2.Noise_Data.watch(full_document='updateLookup')
    document = next(cursor)
    print(document)
    db1.Trigger.update_one({'flag of noise data': '1: changed; 0: not changed.'},{'$inc': {'value': 1}},upsert = True)