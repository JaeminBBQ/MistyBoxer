import requests
import time

def drive(linear_velocity, angular_velocity, drive_time, degree):
    params = {
        "linearVelocity": linear_velocity,
        "angularVelocity": angular_velocity,
        "timeMs": drive_time,
        "degree": degree
    }
    requests.post("http://eve/api/drive/time", params=params)

    time.sleep((drive_time / 1000) + 1)

def speak(text):
    params = {
        "text": text,
        "pitch": 0,
        "speechRate": 0,
        "voice": None,
        "flush": False,
        "utteranceId": None,
        "language": None,
    }
    requests.post("http://eve/api/tts/speak", params=params)

    time.sleep(5)