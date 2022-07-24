import pymongo
client = pymongo.MongoClient("mongodb+srv://chaitanya_007:Chaitanya77@chaitanya.2ixsggw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Chaitanya",
    "email" : "rtrchaitanya3170@gmail.com",
    "surname" : "Nilkanthanawar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )