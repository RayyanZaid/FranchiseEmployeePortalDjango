from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# View = request handler

# Map each view to a URL. So when you get a request at that URL, this function is called
def say_hello(requestObject): 
    # can pull data from DB in here


    return HttpResponse('Hello World')