from flask import Flask,render_template
import requests
import json

app = Flask(__name__)   #Flask is the function and __name__ is a special python variable

def get_meme():
    url = "https://meme-api.com/gimme"
    #send a GET request to the API using the requests.request method and retrieve the response as text
    #parse the JSON response using json.loads to convert it into a Python dictionary
    response = json.loads(requests.request("GET",url).text) 
    #extract the URL of the meme image from the "preview" key of the response. 
    meme_large = response["preview"][-2]    #Specifically, it takes the second-to-last item (indexed as -2) from the "preview" list
    subreddit = response["subreddit"]
    return meme_large,subreddit

@app.route("/") #python decorator with app route->where to go from here
def index():
    meme_pic,subreddit = get_meme()
    return render_template("index.html",meme_pic=meme_pic,subreddit=subreddit)

app.run(host="0.0.0.0",port=80) #run app on specified host with provided port number