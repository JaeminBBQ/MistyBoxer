from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import controller
import time
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@api_view(['GET', 'POST'])
def test(request):
    if request.method == "GET":
        return Response({"test": "success"})
    if request.method == "POST":
        print(request.data)
        return Response({"test": "postsuccess"})

@api_view(['POST'])
def scenario_one(request):
    if request.method == "POST":
        controller.speak("Task Recieved")

        controller.drive(100, 0, 38500, 0)
        controller.drive(0, 50, 4500, 90)

        time.sleep(5)

        controller.drive(0, -50, 4500, 90)
        controller.drive(100, 0, 8947, 0)
        controller.drive(0, -50, 4500, 90)

        time.sleep(5)

        controller.drive(0, -50, 4500, 90)
        controller.drive(100, 0, 45400, 0)

        controller.drive(0, -50, 4500, 90)

        controller.speak("Task Complete")

        return Response({"status": 0})

@api_view(['POST'])
def scenario_two(request):
    if request.method == "POST":
        controller.speak("Task Recieved")

        controller.drive(100, 0, 38500, 0)
        controller.drive(0, 50, 4500, 90)

        time.sleep(5)

        controller.drive(0, 50, 4500, 90)
        controller.drive(100, 0, 39000, 0)

        controller.drive(0, -50, 4500, 90)

        controller.speak("Task Complete")

        return Response({"status": 0})

@api_view(['POST'])
def scenario_three(request):
    if request.method == "POST":
        controller.speak("Task Recieved")

        controller.drive(100, 0, 48000, 0)
        controller.drive(0, -50, 4500, 90)

        time.sleep(5)

        controller.drive(0, -50, 4500, 90)
        time.sleep(1)
        controller.drive(100, 0, 7700, 0)
        controller.drive(0, -50, 4500, 90)

        time.sleep(5)

        controller.drive(0, 50, 4500, 90)
        controller.drive(100, 0, 39570, 0)
        controller.drive(0, -50, 4500, 90)


        controller.speak("Task Complete")

        return Response({"status": 0})

