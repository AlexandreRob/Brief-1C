from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import csv
from .models import *
from dashboard.models import Country, Detailfacture, Invoice, Product



def home(request):
    return render(request, "home.html", {})

def get_data(elements, infos) : 
    InvoiceNo = elements[0]
    StockCode = elements[1]
    Description = elements[2]
    Quantity = elements[3]
    InvoiceDate = elements[4]
    UnitPrice = elements[5]
    CustomerID = elements[6]
    Country = elements[7]
    
    infos["details"] = {}
    infos["details"]["InvoiceNo"] = InvoiceNo
    infos["details"]["StockCode"] = StockCode
    infos["details"]["Description"] = Description
    infos["details"]["Quantity"] = Quantity
    infos["details"]["InvoiceDate"] = InvoiceDate
    infos["details"]["UnitPrice"] = UnitPrice
    infos["details"]["CustomerID"] = CustomerID
    infos["details"]["Country"] = Country
    

def create_data(infos):
    infos["details"] = {}
    infos["details"]["InvoiceNo"]
    infos["details"]["StockCode"]
    infos["details"]["Description"]
    infos["details"]["Quantity"]
    infos["details"]["InvoiceDate"]
    infos["details"]["UnitPrice"]
    infos["details"]["CustomerID"]
    infos["details"]["Country"]


def import_csv(request):
    if request.method == "POST":
        fichier = request.POST['csv']
        

        with open('D:/Documents/Afpar exo/Brief-1C/' + fichier, 'r') as f:
            reader = csv.reader(f)
    return render(request, "import.html", {})
    

def graph1(request): 
    return render(request, "Graph1.html", {})

def graph2(request): 
    return render(request, "Graph2.html", {})

def graph3(request): 
    return render(request, "Graph3.html", {})


# Create your views here.
