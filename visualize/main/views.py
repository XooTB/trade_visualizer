from django.shortcuts import render
from main.models import data
import json


# Create your views here.
def index(request):
    file = open("main/data.json", "r")
    data = json.load(file)

    return render(request, 'main/home.html', {'datas': data} )

def tableview(request):
    datalist = data.objects.all(); 
    return render(request, 'main/tableview.html', {'datas': datalist})
