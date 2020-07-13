
from src.app import app
from pymongo import MongoClient
from src.config import DBURL
from flask import request
import re


@app.route ("/")
def Welcome():
    return "Welcome to the Chat Senrretiment Analysis Service what up fffffcer"

client = MongoClient(DBURL)
print(f"connected to db {DBURL}")
db = client.get_database("PulpFiction")

@app.route("/personaje/create/<personaje>")
def personaje_creation ():
    personaje_nuevo = db.personaje.insert_one({"personaje":personaje}).inserted_id
    return (f" {personaje} is the new character")



@app.route("/personaje/create/<chat>")
def chat_creation ():
    new_chat =db.chats.insert_one({"chat":chat},{"personaje":[]}).inserted_id
    return {f" {chat} is the new chat creator"}

@app.route("/chats/<chat>/<personaje>/")
def crear_chat_personaje(chat,personaje):
    chat_id=db.chats.find_one({"chat":chat})
    db.chats.update_one(
            {"_id":chat_id['_id']},
            {"$push": { "personaje": personaje } }
                               )
    return { "result":
            f"  {personaje}, was added to script {chat}"}


@app.route("/script/", methods=['POST'])
def read_script():
    script=request.get_json()
    if script:
        if consulta_chat(text['chat']):
            if consulta_personaje_chat(script['personaje'],script['chat']):
                res=db.script.insert_one({"personaje":script['personaje'],
                    "chat": mensaje['chat'],
                    "lines": script['lines'] } )
                return  {f"The script is  send with id:{res}"}

            return {"error":"Please check if the user exist and insert the user in the chat"}
     



    
   
     



    



