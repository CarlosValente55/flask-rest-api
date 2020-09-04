import requests
import json
import os
path_to_json = 'data/'

activity_id = {"run": 3 ,"soccer": 25}


def get_data_from_json():
    #Opens all  json files from data folder
    for user_id, json_file_name in enumerate (os.listdir(path_to_json)):
        with open(path_to_json+json_file_name) as json_file:
            #print(path_to_json+json_file_name)
            data = json.load(json_file)
            #print(type(json.dumps(data)))
            request=requests.post("http://127.0.0.1:5000/workout/"+str(user_id)+"/users/"+str(user_id),headers={'Content-Type': 'application/json'},data=json.dumps(data))

get_data_from_json()


