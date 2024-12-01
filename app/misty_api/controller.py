import requests

def drive(linear_velocity, angular_velocity, time, degree):
    params = {
        "linearVelocity": linear_velocity,
        "angularVelocity": angular_velocity,
        "timeMs": time,
        "degree": degree
    }
    requests.post("http://eve/api/drive/time", params=params)