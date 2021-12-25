from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ping(request):
    print("request obejct: ",request)
    return HttpResponse("Hello!! generator app is working.")

