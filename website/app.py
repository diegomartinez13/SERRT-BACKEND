from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
# from apscheduler.schedulers.background import BackgroundScheduler
import os, random, time

app = Flask(__name__)

# # create a scheduler
# scheduler = BackgroundScheduler()

#app secret key:
app.config['SECRET_KEY'] = "af5befba506920bfb443d8e53159d0bd5756a90f"

# app.config["MONGO_URI"] = "mongodb://localhost:27017/solar-car"
# app.config["MONGO_URI"] = "mongodb+srv://admin:admin@carrosolarcluster.o3baw9s.mongodb.net/?retryWrites=true&w=majority"

#Images folder
IMG_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

#Connection to MongoDB server
client = MongoClient("mongodb://localhost:27017/")
db = client['solarcar_database']
data_collection = db['data']

# #Initializing variable that will be used for the simulation
# simulation_data = {}

# # Define the job that will run every 1 minutes
# @scheduler.scheduled_job('interval', minutes=1)
# def scheduled_job():
#     print("scheduler started")
#     #Saving data on a global variable in order to get access to it
#     global simulation_data
#     #Getting lastest data form database
#     simulation_data = data_collection.find_one(sort=[('_id', -1)])
#     simulation_data['_id'] = str(simulation_data['_id'])
#     print("Scheduler ended")

#Route to base dashboard
@app.route('/')
def get_index():
    return render_template('index.html')

#Route to base dashboard
@app.route("/cardata", methods=["GET"])
def get_cardata():
    #Getting lastest data form database
    data = data_collection.find_one(sort=[('_id', -1)])
    data['_id'] = str(data['_id'])
    
    #Rendering data
    return render_template('dashboard.html', optimal_velocity=data.get("optimal_velocity"), solar_panel_output= data.get("solar_panel_output"), current_temp= data.get("current_temp"), current_speed=data.get("current_speed"), battery=data.get("battery"))

#route to dashboard data simulation
@app.route("/cardata/simulation", methods=["GET"])
def get_cardata_simulation():
    #Getting lastest data form database
    data = data_collection.find_one(sort=[('_id', -1)])
    data['_id'] = str(data['_id'])
    return data

#Route to add data to dashboard
@app.route("/add_data", methods=["POST"])
def add_data():
    #Dadding data to database
    data = request.get_json()
    data_collection.insert_one(data)
    return {"message": "Data added successfully"}

# @app.route("/add_data/simulate", methods=["POST"])
# def simulate_data():
#     # Simulate random data
#     optimal_velocity = random.randint(30, 90)
#     current_speed = random.randint(30, 90)
#     current_temp = random.randint(10, 40)
#     battery = random.randint(11, 13)
#     solar_panel_output = random.randint(0, 25)

#     # Insert data into MongoDB
#     data = {
#         'optimal_velocity': optimal_velocity,
#         'current_speed': current_speed,
#         'current_temp': current_temp,
#         'battery': battery,
#         'solar_panel_output': solar_panel_output,
#     }
#     data_collection.insert_one(data)

#     return jsonify({'message': 'Data added successfully'}) 

if __name__ == "__main__":
    app.run(debug=True)
