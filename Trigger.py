import bson
# from pymongo import MongoClient
#
# client1 = MongoClient('mongodb://54.229.58.205:27017')
# db1 = client1.wayfindr
# client2 = MongoClient('mongodb://52.31.97.5:27017')
# db2 = client2.wayfindr
# # collection = db.Noise_Data
#
# # Change Streams in MongoDB
# while(1):
#     cursor = db2.Noise_Data.watch(full_document='updateLookup')
#     document = next(cursor)
#     print(document)
#     db1.Trigger.update_one({'flag of noise data': '1: changed; 0: not changed.'},{'$inc': {'value': 1}},upsert = True)






a = {}
a = {'_id': {'_data': b'\x82Z\xbai\x8d\x00\x00\x00\x02Fd_id\x00dZ\xb1\x13\xf2V\xa0!#&\x078\xcd\x00Z\x10\x04;B\xbc\x8fOEDj\x88\\\x99\r\x95\xa0o\xb8\x04'}, 'operationType': 'update', 'fullDocument': {'_id': '5ab113f256a02123260738cd', 'Position_Number': 12, 'Date': '27/03/2018', 'Noise_Index': '56.73', 'Position_Name': 'Blessington St. Basin', 'Time': '16:50:00'}, 'ns': {'db': 'wayfindr', 'coll': 'Noise_Data'}, 'documentKey': {'_id': '5ab113f256a02123260738cd'}, 'updateDescription': {'updatedFields': {'Noise_Index': '56.73', 'Time': '16:50:00'}, 'removedFields': []}}
b = {}
b = {'_id': {'_data': b'\x82Z\xbakF\x00\x00\x00\x01Fd_id\x00dZ\xb1\x13\xf0V\xa0!#&\x078\x88\x00Z\x10\x04;B\xbc\x8fOEDj\x88\\\x99\r\x95\xa0o\xb8\x04'}, 'operationType': 'update', 'fullDocument': {'_id': '5ab113f056a0212326073888', 'Position_Number': 1, 'Date': '27/03/2018', 'Noise_Index': '52.76', 'Position_Name': 'Drumcondra Library', 'Time': '16:50:00'}, 'ns': {'db': 'wayfindr', 'coll': 'Noise_Data'}, 'documentKey': {'_id': '5ab113f056a0212326073888'}, 'updateDescription': {'updatedFields': {'Noise_Index': '52.76'}, 'removedFields': []}}

print(a['updateDescription'])
print(b['updateDescription'])

aa = a['updateDescription']
aaa = aa['updatedFields']
print(aaa)
print(len(aaa) == 2)
print(type(aaa))
print('Noise_Index' in aaa)
if (len(aaa) == 2) and ('Noise_Index' in aaa):
    print("1")

