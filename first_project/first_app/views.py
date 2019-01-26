from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    my_dict = {'insert_me':"Hello I'm from first_app/views.py and my name is Camila"}
    return render(request,'first_app/index.html',context=my_dict)