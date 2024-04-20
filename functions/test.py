import json
import uuid



def storeValue(parameter: dict):
    # store the parameter dict containing name and birthday in a json file as uuid

    with open('user.json', 'r+') as json_file:
        json_data         = json.load(json_file)
        myuuid            = uuid.uuid4()
        json_data[myuuid] = parameter

        json_file.seek(0)
        json.dump(json_data, json_file, indent=4) 
        json_file.truncate()

    return myuuid

