from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['github_webhooks']
collection = db['events']

# Fetch all documents
data = collection.find()

# Display the documents
for doc in data:
    print(doc)