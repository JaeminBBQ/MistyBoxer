import requests

def drive(linear_velocity, angular_velocity):
    params = {
        "linearVelocity": linear_velocity,
        "angularVelocity": angular_velocity
    }
    requests.post("http://192.168.1.125/api/drive", params=params)