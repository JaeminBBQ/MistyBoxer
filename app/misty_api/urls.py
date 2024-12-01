from django.urls import path
from . import views

urlpatterns = [
    path('scenario1/', views.scenario_one, name="scene1"),
]
