from flask import Flask
from utils.dataParser import parse_data

app = Flask(__name__)

data = parse_data('App/Twitch Clips.txt')
print (data)

@app.route("/")
def hello_world():
    return "hello clip"
