from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<em> My Second Project </em>")

def help(request):
    my_dict = {"message" : "Help Page <3"}
    return render(request, "AppTwo/help.html", context=my_dict)