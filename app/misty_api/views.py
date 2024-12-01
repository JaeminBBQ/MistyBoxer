from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import controller

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
        controller.drive(100, 0, 10000, 0)

        return Response({"status": 0})