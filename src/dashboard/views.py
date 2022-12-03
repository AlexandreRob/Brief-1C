from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import csv
from .models import *



def home(request):
    return render(request, "home.html", {})


def get_InvoiceNo(elements, details):
    facture = elements[0]
    details["details"] = {}
    details["details"]["facture"] = facture

def get_StockCode(elements, details):
    produit = elements[1]
    details["details"] = {}
    details["details"]["produit"] = produit

def get_Description(elements, details):
    description = elements[2]
    details["details"] = {}
    details["details"]["description"] = description

def get_Quantity(elements, details):
    Quantity = elements[3]
    details["details"] = {}
    details["details"]["quantité"] = Quantity

def get_InvoiceDate(elements, details):
    date = elements[4]
    details["details"] = {}
    details["details"]["date"] = date

def get_UnitPrice(elements, details):
    prix = elements[5]
    details["details"] = {}
    details["details"]["prix"] = prix

def get_CustomerID(elements, details):
    CustomerID = elements[6]
    details["details"] = {}
    details["details"]["CustomerID"] = CustomerID

def get_Country(elements, details):
    pays = elements[7]
    details["details"] = {}
    details["details"]["pays"] = pays
    

def create_data(details):
    

def import_csv(request):
        return render(request, "import.html", {})
    

def graph1(request): 
    return render(request, "Graph1.html", {})

def graph2(request): 
    return render(request, "Graph2.html", {})

def graph3(request): 
    return render(request, "Graph3.html", {})


# Create your views here.
