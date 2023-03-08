# MongoDB Insert Functionality

# Go over how to use the various insert functions of the pymongo module.
### Import pymongo, and MongoClient
import pymongo
from pymongo import MongoClient

### Initalize A Client, Connect To DB, Speicfy Collection
client = MongoClient("mongodb://localhost:27017/")
db = client["my_store"]
products_col = db["products"]

### insert()
# *Deprecated, Do Not Use In Your Applications*
bag = {"name": "Bag", "price": 23.78}
insert_res = products_col.insert(bag)
print(insert_res)
phone = {"name": "iPhone 11", "price": 800}
notebook = {"name": "Notebook", "price": 4.99}
insert_res_multiple = products_col.insert([phone, notebook])
print(insert_res_multiple)

### insert_one()
pens = {"name": "Pens", "price": 9.58}
insert_one_res = products_col.insert_one(pens)
print(insert_one_res)
print(insert_one_res.acknowledged)
print(insert_one_res.inserted_id)

### insert_many()
water_bottle = {"name": "Water Bottle", "price": 14.85}
jar = {"name": "Jar", "price": 4.99}
insert_many_res = products_col.insert_many([water_bottle, jar])
print(insert_many_res)
print(insert_many_res.acknowledged)
print(insert_many_res.inserted_ids)

### Error Handling When Inserting
# Produces a DuplicateKeyError
products_col.insert_one(pens)
pens2 = {"name": "Pens", "price": 9.58}
products_col.insert_one(pens2)

# Produces a DuplicateKeyError
pens["price"] = 10.00
products_col.insert_one(pens)

# Produces a BulkWriteError
products_col.insert_many([water_bottle, jar])
try:
    products_col.insert_one(pens)
except pymongo.errors.DuplicateKeyError:
    print("Duplicate Entry Detected")
try:
    products_col.insert_many([water_bottle, jar])
except pymongo.errors.BulkWriteError:
    print("Bulk Write Error Detected")
### insert_many() - Partial Fail Interaction
mug = {"name": "Mug", "price": 12.99}
try:
    products_col.insert_many([mug, jar])
except pymongo.errors.BulkWriteError:
    print("Bulk Write Error Detected")
