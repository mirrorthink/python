
import pymongo
client = pymongo.MongoClient('127.0.0.1',port = 27017)
db = client.zhihu

collection = db.qa
#collection.insert({'username':'test'})
# collection.insert_many([
#     {'1': 2, '2': 3},
#     {'1': 4, '2': 5}
#                        ]
# )
# cursor = collection.find()
# for x in cursor:
#     print(x)

print(collection.find_one({'1':2}))

collection.update_one({'1': 2}, {'$set': {'2': 'ccc'}})
print(collection.find_one({'1':2}))