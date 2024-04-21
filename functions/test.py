import json
import uuid
import os
from .check import internalCheck
import google.generativeai as genai
from dotenv import load_dotenv
from .user import addUser

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API'))
model = genai.GenerativeModel('gemini-pro')


def storeValue(name: str, birthday: str):
    temp = {
        "name": name,
        "birthday": birthday
    }

    # Path to the JSON file
    filepath = 'data/user.json'

    # Initialize the data dictionary
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        json_data = {}
    else:
        with open(filepath, 'r') as json_file:
            json_data = json.load(json_file)

    # Generate a unique identifier
    myuuid = str(uuid.uuid4())

    # Store the parameter under the generated UUID
    json_data[myuuid] = temp

    # Write the updated data back to the file
    with open(filepath, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    
    with open("data/context.json", "r") as json_file:
        json_data = json.load(json_file)
        json_data[myuuid] = {"Q": 0, "initial": [], "context_question": [], "context":[]}
    
    with open("data/context.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)

    return myuuid


def getQuestion(uuid: str):
    questions = [
        "What are your hobbies and interests?",
        "How do you usually spend your weekends?",
        "What's the last book you read or movie you enjoyed watching?",
        "Who are your favorite artists or celebrities?",
        "If you could travel anywhere, where would you go?"
    ]




    # get the value from the json file by uuid
    questionStatus = internalCheck(uuid)
    print(questionStatus)
    if questionStatus == "Done":
        addUser(uuid)
        return "Done"
    else:
        if questionStatus["initial"] == "":
            return questions[questionStatus["Q"]]
        else:
            response = model.generate_content('Ask the user a more indepth question in relation to their previous response' + questions[questionStatus["Q"]] + questionStatus["initial"] + "Generate a question to ask: ")
            return response.text


#### test storeValue function
#-------------------------------
# parameter = {'name': 'John', 'birthday': '1990-01-01'}
# myUUID    = storeValue(parameter)
# with open('user.json', 'r+') as json_file:
#     json_data         = json.load(json_file)
#     print(json_data)
# sample_user = {"name": "John", "birthday": "1990-01-01"}
# sample_uuid = storeValue(sample_user)


# output = getQuestion(sample_uuid)
# #print(output)

# uuid = "a8b316c1-689d-47bb-afde-32cd6ea50859"
# output=getQuestion(uuid)
# print(output)