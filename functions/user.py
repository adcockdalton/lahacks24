import chromadb
import json


chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="users")

def addUser(uuid):
    collection = chroma_client.get_or_create_collection(name="users")

    with open("data/context.json", 'r') as json_file:
        json_data = json.load(json_file)
        user = json_data[uuid]
    collection.add(
        documents=str(user),
        ids=uuid
    )

    print(collection.peek())