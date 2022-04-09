import json
import os

def login(username=str, password=str):
    if os.path.exists("users/"+username+".json")==True:
        #check password

        #load user data
        with open("users/"+username+".json") as user_file:
           user_data = json.load(user_file)

        user_password=""
        for p in user_data["userdata"]:   
            user_password=p["password"]

        if(password==user_password):
            return True
        else:
            return False    
    else:
        return False

def register(username=str, password=str, name=str):
    new_user_data= {}
    new_user_data['userdata']=[]
    new_user_data["userdata"].append({
            'name':name,
            'username':username,
            'password':password
    })

    #create user file
    user_file=open("users/"+username+".json", "w")
    json.dump(new_user_data,user_file)
    user_file.close()