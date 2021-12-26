from django.urls import path
from . import views

urlpatterns = [
    path('ping', view=views.ping, name='ping'),
    path('multi-ping',view=views.multi_ping, name='multi-ping')
]