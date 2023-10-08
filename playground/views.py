from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

# View = request handler

# Map each view to a URL. So when you get a request at that URL, this function is called


def say_hello(request):
    # Create a Python dictionary representing your JSON data
    data = {'name': 'Rayyan'}

    # Use JsonResponse to convert the dictionary to a JSON response
    return JsonResponse(data)
 