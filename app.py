from flask import Flask,Response,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return Response('working')