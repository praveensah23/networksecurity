
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb://praveensah23:<password>@ac-7i1mewf-shard-00-00.bp2fktj.mongodb.net:27017,ac-7i1mewf-shard-00-01.bp2fktj.mongodb.net:27017,ac-7i1mewf-shard-00-02.bp2fktj.mongodb.net:27017/?ssl=true&replicaSet=atlas-abefs9-shard-0&authSource=admin&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)