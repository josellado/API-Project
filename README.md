# API-Project
## Part One : Api Service
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSXRHXpwW3vMkAt-p3iFc2j7nPvVmPt30ZO4g&usqp=CAU">

The purpose of these project  is to extract the sentiment metrics of some of the most iconic quotes of PulFiction. 

To do so, we are going to create an api service, these service will call the api endpoints previously created. 

The steps followed were the following:

1) Connect local host with mongodb 
- url = f"http://localhost:3000/"

2) Upload the characters do the Api
- @app.route("/personaje/create/<name>")


3) Create a chat
- @app.route("/chat/create")

4) Add characters to the chat
- @app.route("/personaje/<conversation_id>/addcharacter")

5) Add The quotes said by each character
- @app.route("chat/converstion_id/addquote/", methods=['POST'])

## Part 2 : Sentimenal Analysis

<img src = "https://pbs.twimg.com/media/EHvjm5NX0AI9CNI.jpg">
 
 The second part of these project will analyse the quotes Using "NLTK" sentiment analysis package. 
 The idea is to find out if the words used by the characters represent the same emotions as there expresions








