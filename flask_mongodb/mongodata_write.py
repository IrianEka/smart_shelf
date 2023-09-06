import pymongo
from pymongo.mongo_client import MongoClient

password = "SGzkyaxsykdPzYYf"
uri = "mongodb+srv://irianeka21:<password>@jayamahe.nnvynod.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)
db = client['test']
my_collection = db['test_collection']

lcd1 = {'address': '0x25', 'line1': 'Mi gooreng A', 'line2': 'Rp. 3.500'}
lcd2 = {'address': '0x26', 'line1': 'Susu A', 'line2': 'Rp. 4.500'}
lcd3 = {'address': '0x27', 'line1': 'Sabun A', 'line2': 'Rp. 10.500'}

results = my_collection.insert_many([lcd1, lcd2, lcd3])
print(results.inserted_ids)