from flask import Flask, render_template
import requests 
import json

app = Flask(__name__)

@app.route("/")
def get_quote():
    r = requests.get("https://api.quotable.io")
    quotejson = r.json()

    print(quotejson['content'])
    return render_template('index.html')