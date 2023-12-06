from django.shortcuts import render
from main.models import data
import json
import time
from datetime import datetime

def distict(data):
    appendedCodes = []
    datas = []
    for i in data:
        if i.trade_code not in appendedCodes:
            datas.append(i)
            appendedCodes.append(i.trade_code)
    return datas

# Create your views here.
def index(request):
    file = open("main/data.json", "r")
    data = json.load(file)

    return render(request, 'main/home.html', {'datas': data} )

def tableview(request):
    datalist = data.objects.all().order_by('trade_code')
    datalist = distict(datalist)

    return render(request, 'main/tableview.html', {'datas': datalist})


def detailedView(request, tradeCode):
    datas = data.objects.all().filter(trade_code=tradeCode).order_by('date')
    stepcount = []
    candleData = []
    for i in datas:
        stepcount.append({"y": i.close, "label": str(i.date)})

    for i in datas:
        utime = time.mktime(datetime.strptime(str(i.date), "%Y-%m-%d").timetuple()) * 1000
        candleData.append({"x": utime , "y": [i.open, i.high, i.low, i.close]})

    return render(request, 'main/detailedView.html', {'datas': datas, 'tradeCode': tradeCode, "stepcount": stepcount, "candleData": candleData})