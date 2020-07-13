
from src.app import app
from pymongo import MongoClient
from src.config import DBURL
from flask import request
import re
from bson.json_util import dumps
import requests

@app.route ("/")
def Welcome():
    return "Welcome to the Chat Senrretiment Analysis Service what up fffffcer"

client = MongoClient(DBURL)
print(f"connected to db {DBURL}")
db = client.get_database()#["PulpFiction"]
"""
@app.route("/user/create/<personaje>")
def personaje_creation (personaje):
    personaje_nuevo = db.user.insert_one({"personaje":personaje})
    res={"user_id":str(personaje_nuevo)}
    return dumps(f" {personaje} is the new character")

"""
@app.route("/personaje/create/<name>")
def create_user(name):
    new_character= {"name": name}
    already_user= db.user.distinct("name")
    if name in already_user:
        raise ValueError ("This character already exists. Add another name.")
    else:
        add_character = db.user.insert_one(new_character)
        return dumps(f"New user create! user_name:{name}, user_id: {add_character.inserted_id} ")   

    
@app.route("/chat/create")
def scene_creation ():
    characters_scene = request.args.getlist("participants")
    scene = request.args.get("scene")
    new_scene =db.scene.insert({"scene":scene,"participants":characters_scene})
    return dumps(f"{new_scene} is the new chat creator")



@app.route("/personaje/<conversation_id>/addcharacter")
def add_character(conversation_id):
    new_character = request.args.get("user_name")
    check_character = list(db.dialogo.find({"id": ObjectId(conversation_id),"participants":new_character}))
    add_character = db.dialogo.update({"id":ObjectId(conversation_id)}, {"$push":{"participants":new_character}})
    return dumps (f"{check_character} has entered the scene {add_character}")



"""

@app.route("chat/converstion_id/addquote/", methods=['POST'])
def read_script(conversation_id):
    conver=request.form.get("conversation_id")
    user = request.form.get("user_name")
    mensaje = request.form.get("message")
    add_message = db.script.insert ({"conversation_id":ObjectId(conversation_id), "user_id":ObjectId(user), "message":f'{mensaje}'})
    return dumps (f" added new line , id message {add_message}")
         
  """  


  
   
     



    



