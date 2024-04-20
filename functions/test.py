import json
import uuid
import os

def storeValue(parameter: dict):
    # Path to the JSON file
    filepath = 'user.json'

    # Initialize the data dictionary
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        json_data = {}
    else:
        with open(filepath, 'r') as json_file:
            json_data = json.load(json_file)

    # Generate a unique identifier
    myuuid = str(uuid.uuid4())

    # Store the parameter under the generated UUID
    json_data[myuuid] = parameter

    # Write the updated data back to the file
    with open(filepath, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    return myuuid


def getValue(uuid: str):
    # get the value from the json file by uuid

    with open('user.json', 'r') as json_file:
        json_data = json.load(json_file)
        return json_data[uuid]

parameter = {'name': 'John', 'birthday': '1990-01-01'}
myUUID    = storeValue(parameter)
with open('user.json', 'r+') as json_file:
    json_data         = json.load(json_file)
    print(json_data)