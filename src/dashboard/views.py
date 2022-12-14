from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import csv
import pandas as pd
import sqlalchemy
import psycopg2
import psycopg2.extras as extras
from .models import *
from django.conf import settings
from dashboard.models import *
from .form import UploadFileForm




def home(request):
    return render(request, "home.html", {})


def import_csv(request):
    return render(request, "import.html", {})
        
    

def page_csv(request):
    return render(request, "import.html", {})
    

def topG1(request): 
    sql = '''SELECT product.stockcode, count(*)
                FROM product
                INNER JOIN detailfacture on product.stockcode = detailfacture.stockcode
                GROUP BY product.stockcode
                ORDER BY count DESC
                LIMIT 10'''
        
    
    res = Product.objects.raw(sql)
  
    return render(request, "Graph1.html", {'data': res})

def test(request):
    sql = '''SELECT product.stockcode, count(*)
                FROM product
                INNER JOIN detailfacture on product.stockcode = detailfacture.stockcode
                GROUP BY product.stockcode
                ORDER BY count DESC
                LIMIT 10'''
        
    
    res = Product.objects.raw(sql)
    return render(request, "test.html", {'data': res})

def flopG1(request): 
    sql = '''SELECT product.stockcode, count(*)
                FROM product
                INNER JOIN detailfacture on product.stockcode = detailfacture.stockcode
                GROUP BY product.stockcode
                ORDER BY count ASC
                LIMIT 10'''
        
    
    res = Product.objects.raw(sql)
  
    return render(request, "Graph1flop.html", {'data' : res})

def topG2(request): 
    sql = '''SELECT country, count(*)
                FROM detailfacture
                INNER JOIN invoice on detailfacture.invoiceno = invoice.invoiceno
                GROUP BY invoice.country
                ORDER BY count DESC
                LIMIT 10'''

    res = Country.objects.raw(sql)
    
    return render(request, "Graph2.html", {'data': res})

def G2no(request):
    sql = '''SELECT country, count(*)
                FROM detailfacture
                INNER JOIN invoice on detailfacture.invoiceno = invoice.invoiceno
                WHERE country <> 'United Kingdom'
                GROUP BY invoice.country
                ORDER BY count DESC
                LIMIT 10'''
    res = Country.objects.raw(sql)

    return render(request, 'Graph2no.html', {'data': res})

def flopG2(request): 
    sql = '''SELECT country, count(*)
                FROM detailfacture
                INNER JOIN invoice on detailfacture.invoiceno = invoice.invoiceno
                GROUP BY invoice.country
                ORDER BY count ASC
                LIMIT 10'''

    res = Country.objects.raw(sql)
    
    return render(request, 'Graph2flop.html', {'data' : res})

def graph3(request):
    res = {}
    return render(request, "Graph3.html", {'data': res})


# Create your views here.
