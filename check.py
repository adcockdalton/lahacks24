import json

def internalCheck(id: str):

    json_data = None 
    with open('context.json', 'r+') as json_file:
        json_data         = json.load(json_file)

        if len(json_data[id]) == 5:
            return "Done"
        else:
            if json_data[id]["Q"] != len(json_data[id]["initial"]):
                    return {"Q": json_data[id]["Q"], "initial": "", "context":""}
            elif json_data[id]["Q"] != len(json_data[id]["context"]):
                return {"Q": json_data[id]["Q"], "initial": json_data[id]["initial"][json_data[id]["Q"]-1], "context":""}
            else:

                json_data[id]["Q"] += 1
                json_file.seek(0)  # Move file pointer to the start of the file
                json.dump(json_data, json_file)
                json_file.truncate() 
                return {"Q": json_data[id]["Q"], "initial": "", "context":""}
        

print(internalCheck("7314bb45-03f0-4349-9e74-9784b328fa85"))
print(internalCheck("db9fdb03-9e18-49d1-a1b1-32e4ae4d79c6"))
print(internalCheck("bbc2b7ea-0a38-4a11-9e73-380f06937b54"))
