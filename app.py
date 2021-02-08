from flask import Flask 
from flask_cors import CORS 
import pymongo 
import os
from flask import Flask , render_template, jsonify, request, redirect, url_for,jsonify, abort

# Replace your URL here. Don't forget to replace the password. 
#connection_url = process.env.MONGODB_URL
#'mongodb+srv://abin:dbpassword@cluster0.b8byd.mongodb.net/test?retryWrites=true&w=majority'
connection_url = os.environ.get('MONGODB_URL')
print('code is running')
print(connection_url)
app = Flask(__name__) 
client = pymongo.MongoClient(connection_url) 

# Database 
Database = client.get_database('Example') 
# Table 
SampleTable = Database.SampleTable 

mydict = { "name": "Abin", "address": "Highway 37" }

SampleTable.insert_one(mydict)

@app.route('/')
def home():
        return render_template('home.html')

print('successful')

if __name__ == '__main__': 
	app.run(debug=True) 
