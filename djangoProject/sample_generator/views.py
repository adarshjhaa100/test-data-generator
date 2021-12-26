from django.shortcuts import render
from django.http import HttpResponse
from .col_scripts import generate_fibonacci 
from datetime import datetime
from multiprocessing import Pool


# Create your views here.
def ping(request):
    start_time=datetime.now()
    n=100000
    generate_fibonacci.fibonacci(n)
    generate_fibonacci.fibonacci(n)
    generate_fibonacci.fibonacci(n)
    generate_fibonacci.fibonacci(n)
    generate_fibonacci.fibonacci(n)
    print("time elapsed:", datetime.now()-start_time)

    # print("request object: ",request)
    return HttpResponse(f"time elapsed:{datetime.now()-start_time} ")

# Create your views here.
def multi_ping(request):
    n=100000
    start_time=datetime.now()
    with Pool() as p:
        p.map(generate_fibonacci.fibonacci, [n,n,n,n,n])

    print("time elapsed:", datetime.now()-start_time)
    
    # print("request object: ",request)
    return HttpResponse(f"time elapsed:{datetime.now()-start_time}")

