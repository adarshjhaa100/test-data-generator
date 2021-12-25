from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.ping, name='ping')
]