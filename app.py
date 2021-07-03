from flask import Flask,Response,jsonify,request

app = Flask(__name__)

@app.route("/")
def index():
    return 'working'

@app.route("/",methods=['POST'])
def sum():
    """
    sends back the sum of a and b provided in request json
    """
    response = {"sum":request.json['a']+request.json['b']}
    return jsonify(response)

@app.route("/uppercase/<string:search>",methods=['GET'])
def uppercase(search):
    """
    responds with the uppercase version of the url query
    """
    return search.upper()