import pymongo

client=pymongo.MongoClient('mongodb://localhost:27017')

# Connect to your database
db = client["loginPage"]

# Connect to your collection
collection = db["users"]



# Insert a single document
# user = {"name": "anurag",  "password": "password123"}

# collection.insert_one(user)

# documents = [
#     {"name": "john_doe", "password": "pass123"},
#     {"name": "jane_smith", "password": "smith2020"},
#     {"name": "alice_jones", "password": "alice@789"},
#     {"name": "bob_brown", "password": "brownbob"},
#     {"name": "charlie_black", "password": "charlie_black123"},
#     {"name": "david_white", "password": "david_white_pass"},
#     {"name": "eva_green", "password": "evagreen_2021"},
#     {"name": "frank_young", "password": "franky123"},
#     {"name": "grace_lee", "password": "lee_grace456"},
#     {"name": "henry_clark", "password": "henry_789"}
# ]

# # Insert documents into the collection
# collection.insert_many(documents)

print("1.Create\n2.Find\n3.Update\n4.delete ")


number=int(input("enter the number: "))

if number==1:
    name=input("enter the name: ")
    password=input("enter the password: ")
    collection.insert_one({"name": name,  "password": password})
    print("successfully added")
    
elif number==2:
    name=input("enter the name: ")
    if collection.find_one({"name": name}):
        print("yes it exists")
    else:
        print("Not found")
    
elif number==3:
        print("1.Update name\n2.update password")
        update=int(input("what u wanna update: "))
        if update==1:
            name=input("enter the name: ")
            updatedName=input("enter the updated name: ")
            collection.update_one({ "name": name},{"$set": { "name": updatedName } })
            print("successfully Updated name")
        elif update==2:
            name=input("enter the name: ")
            updatedpassword=input("enter the updated password: ")
            collection.update_one({ "name": name},{"$set": { "password": updatedpassword } })
            print("successfully Updated password")
elif number==4:
    name=input("enter which name u wanna delete ")
    collection.delete_one({"name":name})
    print("successfully deleted")
    
additional=input("enter yes if u want to know about number of users: ")

AllCollections = collection.find()

if additional=="yes":
    for document in AllCollections:
        print(document['name'])
    
