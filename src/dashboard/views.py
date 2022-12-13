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




def home(request):
    return render(request, "home.html", {})


def import_csv(request):
        file_csv = "D:\Documents\Afpar exo\Brief-1C\data.csv"
        df = pd.read_csv(file_csv)

        SuppQuantity = df[df['Quantity'] < 0 ].index
        df.drop(SuppQuantity , inplace=True)  #Efface quantité < 0

        SuppPrix = df[df["UnitPrice"]== 0].index
        df.drop(SuppPrix , inplace=True)  #Efface prix unitaire = 0

        SuppPunsp = df[df["Country"] == "Unspecified"].index
        df.drop(SuppPunsp , inplace=True) #Efface les pays = a Unspecified

        df.drop_duplicates(subset= ['InvoiceNo', 'StockCode'], inplace = True)

        df = df.drop(["Description","InvoiceDate","CustomerID"], axis=1)
        df.columns = df.columns.str.lower()

        # engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost/DB_AFPAR01')
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']

        db_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(user=user, password=password,
        database_name=database_name)
        
        engine = sqlalchemy.create_engine(db_url, echo=False)
        df.to_sql(Invoice,if_exists='append', con = engine, index=False)
        
    

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

def flopG1(request): 
    sql = '''SELECT product.stockcode, count(*)
                FROM product
                INNER JOIN detailfacture on product.stockcode = detailfacture.stockcode
                GROUP BY product.stockcode
                ORDER BY count DESC
                LIMIT 10'''
        
    
    res = Product.objects.raw(sql)
  
    return render(request,)

def topG2(request): 
    sql = '''SELECT country, count(*)
                FROM detailfacture
                INNER JOIN invoice on detailfacture.invoiceno = invoice.invoiceno
                GROUP BY invoice.country
                ORDER BY count DESC
                LIMIT 10'''

    res = Country.objects.raw(sql)
    
    return render(request, "Graph2.html", {'data': res})

def flopG2(request): 
    sql = '''SELECT country, count(*)
                FROM detailfacture
                INNER JOIN invoice on detailfacture.invoiceno = invoice.invoiceno
                GROUP BY invoice.country
                ORDER BY count ASC
                LIMIT 10'''

    res = Country.objects.raw(sql)
    
    return render(request)

def graph3(request): 
    return render(request, "Graph3.html", {})


# Create your views here.
