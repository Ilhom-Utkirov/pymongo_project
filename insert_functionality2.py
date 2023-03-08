import pymongo
from pymongo import MongoClient

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


### InsertOne()
pens = {"name": "Pens", "price": 9.50}
insert_one_res = products_col.insert_one(pens)
print(insert_one_res.acknowledged)
print(insert_one_res.inserted_id) # returns id

##error handling
pens2 = {"name": "Pens", "price": 9.50}
#products_col.insert_one(pens) #duplicate error you should endter different object pen2 with same name
products_col.insert_one(pens2)

#what if change attribute and insert?? No
# pens["price"] = 234234
# products_col.insert_one(pens) #duplicate key error collection

### insert_many()
water_bottle = {"name": "Water Bottle", "price": 14.85}
jar = {"name": "Jar", "price": 4.99}
insert_many_res = products_col.insert_many([water_bottle, jar])
print(insert_many_res)
print(insert_many_res.acknowledged)
print(insert_many_res.inserted_ids)

# products_col.insert_many([water_bottle, jar]) #BulkWriteError: batch op errors occurred,
try:
    products_col.insert_one(pens)
except pymongo.errors.DuplicateKeyError:
    print("Duplicate Key Detected")

try:
    products_col.insert_many([water_bottle, jar])
except pymongo.errors.BulkWriteError:
    print("Bulk Key Detected")

pens3 = {"name": "Pens", "price": 9.50}
mug = {"name":"mug", "price":123}
products_col.insert_many([mug, jar, pens3]) #after first error insertion is stopped
