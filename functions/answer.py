import json
from check import internalCheck

def storeAnswer(id: str, answer: str):
    json_data = None 
    with open('context.json', 'r+') as json_file:
        json_data         = json.load(json_file)

        data = internalCheck(id)

        if data["initial"] == "":
            json_data[id]["initial"].append(answer)
        else:
            json_data[id]["context"].append(answer)
        
        json_file.seek(0)  # Move file pointer to the start of the file
        json.dump(json_data, json_file)
        json_file.truncate() 


#storeAnswer("bbc2b7ea-0a38-4a11-9e73-380f06937b54", "Hello")