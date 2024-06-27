from flask import Flask, render_template
import requests 
import json

app = Flask(__name__)

@app.route("/")
def get_quote():
    r = requests.get("https://api.quotable.io/random")
    quotejson = r.json()

    print(quotejson["content"])
    print(quotejson["author"])

    quote = {
        "content" : quotejson["content"], 
        "author": quotejson["author"]
    }

    return render_template('index.html', quote = quote)
