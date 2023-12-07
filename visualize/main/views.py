from django.shortcuts import render
from main.models import data
import json
import time
from datetime import datetime
import os

def distict(data):
    """
    Returns a list of distinct elements from the given data.

    Parameters:
    - data: A list of elements to be processed.

    Returns:
    - A list of distinct elements from the given data.
    """
    appendedCodes = []
    datas = []
    for i in data:
        if i.trade_code not in appendedCodes:
            datas.append(i)
            appendedCodes.append(i.trade_code)
    return datas

def arrangeData(open, high, low, close):
    """
    Arrange the data by converting string values to float.

    Parameters:
    open (str or float): The opening price.
    high (str or float): The highest price.
    low (str or float): The lowest price.
    close (str or float): The closing price.

    Returns:
    list: A list containing the arranged data [open, high, low, close].
    """
    if(type(open) == str):
        open = float(open.replace(",", '.', 0).replace(",", ''))
    if(type(high) == str):
        high = float(high.replace(",", '.', 0).replace(",", ''))
    if(type(low) == str):
        low = float(low.replace(",", '.', 0).replace(",", ''))
    if(type(close) == str):
        close = float(close.replace(",", '.', 0).replace(",", ''))

    return [open, high, low, close]

# Create your views here.
def index(request):
    """
    Renders the home page with data from a JSON file.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template with the loaded data from the JSON file.
    """
    file = open(os.path.dirname(os.path.realpath(__file__)) + '/data.json', 'r')
    data = json.load(file)

    return render(request, 'main/home.html', {'datas': data})

def tableview(request):
    """
    Renders a table view of the data objects.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template with the data objects.

    """
    datalist = data.objects.all().order_by('trade_code')
    datalist = distict(datalist)

    return render(request, 'main/tableview.html', {'datas': datalist})


def detailedView(request, tradeCode):
    """
    Renders a detailed view of the data for a specific trade code.

    Args:
        request (HttpRequest): The HTTP request object.
        tradeCode (str): The trade code to filter the data.

    Returns:
        HttpResponse: The rendered HTML response.

    """
    datas = data.objects.all().filter(trade_code=tradeCode).order_by('date')
    stepcount = []
    candleData = []
    for i in datas:
        if(type(i.close) == str):
            close = float(i.close.replace(",", '.', 0).replace(",", ''))
        else: 
            close = i.close
        
        stepcount.append({"y": close, "label": str(i.date)})

    for i in datas:
        utime = time.mktime(datetime.strptime(str(i.date), "%Y-%m-%d").timetuple()) * 1000
        candleData.append({"x": utime , "y": arrangeData(i.open, i.high, i.low, i.close)})

    return render(request, 'main/detailedView.html', {'datas': datas, 'tradeCode': tradeCode, "stepcount": stepcount, "candleData": candleData})