from flask import Flask 
from flask_cors import CORS 
import pymongo 

# Replace your URL here. Don't forget to replace the password. 
connection_url = 'mongodb+srv://abin:dbpassword@cluster0.b8byd.mongodb.net/test?retryWrites=true&w=majority'

app = Flask(__name__) 
client = pymongo.MongoClient(connection_url) 

# Database 
Database = client.get_database('Example') 
# Table 
SampleTable = Database.SampleTable 

mydict = { "name": "Abin", "address": "Highway 37" }

x = SampleTable.insert_one(mydict)

print('successful')

if __name__ == '__main__': 
	app.run(debug=True) 