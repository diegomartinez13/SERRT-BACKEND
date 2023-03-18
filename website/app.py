from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS
import os

app = Flask(__name__)

#app secret key:
app.config['SECRET_KEY'] = "af5befba506920bfb443d8e53159d0bd5756a90f"

# app.config["MONGO_URI"] = "mongodb://username:password@host:port/database"
app.config["MONGO_URI"] = "mongodb+srv://admin:admin@carrosolarcluster.o3baw9s.mongodb.net/?retryWrites=true&w=majority"

#Images folder
IMG_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

mongo = PyMongo(app)

CORS(app)
db = mongo.db

@app.route('/')
def get_index():
    Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('index.html', website_logo=Logo)

@app.route("/cardata")
def get_cardata():
    # data = mongo.db.data.find()
    return render_template('datasite.html')

@app.route("/upload-data", methods=["POST"])
def add_cardata():
    print(request.json)
    # data = request.get_json()
    # mongo.db.data.insert(data)
    return jsonify({"message": "Data added successfully"})

if __name__ == "__main__":
    app.run(debug=True)
