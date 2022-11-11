from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('replicas/', ReplicaListApiView.as_view()),
    path('index/', index),
    path('ordertours', OrderTourListApiView.as_view())
]
