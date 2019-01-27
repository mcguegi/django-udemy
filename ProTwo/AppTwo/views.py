from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.


def index(request):
    return HttpResponse("<em> My Second Project </em>")

def help(request):
    my_dict = {"message" : "Help Page <3"}
    return render(request, "AppTwo/help.html", context=my_dict)

def users(request):
    user_info = User.objects.order_by("first_name")
    user_dict = {"first_name":user_info}
    return render(request, "AppTwo/users.html", context=user_dict)