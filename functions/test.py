import json




def storeValue(parameter):
    with open('user.json', 'r+') as json_file:
        json_data         = json.load(json_file)
        json_data['user'] = parameter

        json_file.seek(0)
        json.dump(json_data, json_file, indent=4) 
        json_file.truncate()