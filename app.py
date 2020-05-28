from flask import Flask,request,jsonify,make_response
import json
import requests

url="http://numbersapi.com/"

app = Flask(__name__)
@app.route('/', methods = ['GET'])

def home():
	return "Hello"

@app.route('/', methods = ['POST'])

def post():
	req=request.get_json(silent=True,force=True)
	print(req)
	intent = req.get('queryResult').get('intent').get('displayName')
	if(intent=='Default Welcome Intent'):
		return jsonify({'fulfillmentText': 'Welcome'})
	elif(intent=='numbers'):
		types = req.get('queryResult').get('parameters').get('type')
		number = req.get('queryResult').get('parameters').get('number')
		new_url = url+str(int(number))+"/"+types+"?json"
		print(new_url) 
		res = requests.get(new_url)
		dictionary = res.json()["text"]
		return jsonify({'fulfillmentText': dictionary})

if(__name__ == "__main__"):
	app.run(debug=True)

