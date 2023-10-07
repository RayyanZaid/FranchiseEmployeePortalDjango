from django.urls import path, URLPattern
from . import views # from the current folder
from typing import List

# array of URLPatterns
# URL Configuration
urlpatterns : List[URLPattern]  = [

         # the url the user has to access       # the view that is run (reference to the function)
    path(        'hello/',               views.say_hello)

]