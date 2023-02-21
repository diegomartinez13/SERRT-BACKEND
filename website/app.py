from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)

#app secret key:
app.config['SECRET_KEY'] = "af5befba506920bfb443d8e53159d0bd5756a90f"

# app.config["MONGO_URI"] = "mongodb://username:password@host:port/database"
app.config["MONGO_URI"] = "mongodb+srv://admin:admin@carrosolarcluster.o3baw9s.mongodb.net/?retryWrites=true&w=majority"

mongo = PyMongo(app)

CORS(app)
db = mongo.db

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route("/car-data", methods=["GET"])
def get_cardata():
    # data = mongo.db.data.find()
    return "done"

@app.route("/upload-data", methods=["POST"])
def add_cardata():
    print(request.json)
    # data = request.get_json()
    # mongo.db.data.insert(data)
    return jsonify({"message": "Data added successfully"})

if __name__ == "__main__":
    app.run(debug=True)
