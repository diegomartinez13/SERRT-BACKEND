"""
Author: Diego Martinez Garcia

Description: Python Script that sends POST requests with random data in order to simulate data colection from the solar car.
The data will be send every 5 seconds in order to get a better simulation.

"""
import requests, random, time

#URL where the data will be send
URL = "http://localhost:5000/add_data"

def get_random_data():
    #Random data generarion
    velocity = random.randint(10,45)
    speed = random.randint(10,45)
    temp = random.randint(60,84)
    battery = random.randint(25,99)
    solar = random.randint(80, 120)

    #Saving data on dictionary
    data = {"optimal_velocity": velocity, "current_speed": speed, "current_temp": temp, "battery": battery, "solar_panel_output": solar}

    return data


def send_data():
    #Gathering data
    data = get_random_data()

    #POST request response
    response = requests.post(url=URL, json=data)

    return response

def main():
    while True:
        #Saving response of POST request
        send_data()
        time.sleep(1)


if __name__ == "__main__":
    #Running code
    main()
