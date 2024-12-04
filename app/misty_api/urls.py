from django.urls import path
from . import views

urlpatterns = [
    path('scenario1/', views.scenario_one, name="scene1"),
    path('scenario2/', views.scenario_two, name="scene2"),
    path('scenario3/', views.scenario_three, name="scene3"),
]
