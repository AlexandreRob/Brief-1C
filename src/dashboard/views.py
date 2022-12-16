from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
import csv
import pandas as pd
import sqlalchemy
import psycopg2
import psycopg2.extras as extras
from .models import *
from django.conf import settings
from dashboard.models import *
from .forms import UploadFileForm
from io import TextIOWrapper




def home(request):
    return render(request, "home.html", {})


def produit(df):
    df = df
    ######################################################################### Nettoyage df
    indexNames = df[df["Country"] == "Unspecified"].index
    df.drop(indexNames , inplace=True) #Efface les pays = a Unspecified

    df.drop(df[df['InvoiceNo'].str.len() > 6].index, inplace = True)
    SuppQuantity = df[df['Quantity'] < 0 ].index
    df.drop(SuppQuantity , inplace=True)  #Efface quantité < 0

    SuppPrix = df[df["UnitPrice"]== 0].index
    df.drop(SuppPrix , inplace=True)  #Efface prix unitaire = 0
    
    indexNames = df[df['StockCode'].str.match('^A-Za-z')==True].index
    df.drop(indexNames , inplace=True) #Efface stockcode composer de A-Z et a-z
    df.drop_duplicates(subset= ['InvoiceNo', 'StockCode'], inplace = True)
    #Efface les doublon commun de la colonne facture et produit

    ######################################################################### Table Product
    product = df
    product = product.drop(['Country','InvoiceNo','UnitPrice','Quantity','CustomerID','InvoiceDate'], axis=1)
    product.drop_duplicates("StockCode", keep = 'first', inplace= True)
    product.columns = product.columns.str.lower()

    ######################################################################### Connexion db
    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']

    db_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(user=user, password=password,
    database_name=database_name)
    
    engine = sqlalchemy.create_engine(db_url, echo=False)

    product.to_sql("product",if_exists='append', con = engine, index=False)

def detailfacture(df):
    ######################################################################### Nettoyage df
    df = df
    indexNames = df[df["Country"] == "Unspecified"].index
    df.drop(indexNames , inplace=True) #Efface les pays = a Unspecified

    df.drop(df[df['InvoiceNo'].str.len() > 6].index, inplace = True)
    SuppQuantity = df[df['Quantity'] < 0 ].index
    df.drop(SuppQuantity , inplace=True)  #Efface quantité < 0

    SuppPrix = df[df["UnitPrice"]== 0].index
    df.drop(SuppPrix , inplace=True)  #Efface prix unitaire = 0
    
    indexNames = df[df['StockCode'].str.match('^A-Za-z')==True].index
    df.drop(indexNames , inplace=True) #Efface stockcode composer de A-Z et a-z
    df.drop_duplicates(subset= ['InvoiceNo', 'StockCode'], inplace = True)
    #Efface les doublon commun de la colonne facture et produit

    ######################################################################### Table detailfacture
    detailfacture = df
    detailfacture = detailfacture.drop(['Country', 'Description','CustomerID','InvoiceDate'], axis=1)
    detailfacture.columns = detailfacture.columns.str.lower()

    ######################################################################### Connexion db
    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']

    db_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(user=user, password=password,
    database_name=database_name)
    
    engine = sqlalchemy.create_engine(db_url, echo=False)
    ######################################################################### Envoie dans db
    detailfacture.to_sql("detailfacture",if_exists='append', con = engine, index=False)

def invoiceno(df):
    df = df
    ######################################################################### Nettoyage df
    indexNames = df[df["Country"] == "Unspecified"].index
    df.drop(indexNames , inplace=True) #Efface les pays = a Unspecified

    df.drop(df[df['InvoiceNo'].str.len() > 6].index, inplace = True)
    SuppQuantity = df[df['Quantity'] < 0 ].index
    df.drop(SuppQuantity , inplace=True)  #Efface quantité < 0

    SuppPrix = df[df["UnitPrice"]== 0].index
    df.drop(SuppPrix , inplace=True)  #Efface prix unitaire = 0
    
    indexNames = df[df['StockCode'].str.match('^A-Za-z')==True].index
    df.drop(indexNames , inplace=True) #Efface stockcode composer de A-Z et a-z
    df.drop_duplicates(subset= ['InvoiceNo', 'StockCode'], inplace = True)
    #Efface les doublon commun de la colonne facture et produit
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate']).dt.date
    # Change format date without heure

    ######################################################################### Table Product
    invoiceno = df
    invoiceno = invoiceno.drop(['Description','Quantity','UnitPrice','Description','StockCode','CustomerID'], axis=1)
    invoiceno.drop_duplicates("InvoiceNo", keep = 'first', inplace= True)
    invoiceno.columns = invoiceno.columns.str.lower()

    ######################################################################### Connexion db
    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']

    db_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(user=user, password=password,
    database_name=database_name)
    
    engine = sqlalchemy.create_engine(db_url, echo=False)
    ######################################################################### Envoie dans db
    invoiceno.to_sql('invoice',if_exists='append', con = engine, index=False)
 
def country(df):
    df = df
    ######################################################################### Nettoyage df
    indexNames = df[df["Country"] == "Unspecified"].index
    df.drop(indexNames , inplace=True) #Efface les pays = a Unspecified

    df.drop(df[df['InvoiceNo'].str.len() > 6].index, inplace = True)
    SuppQuantity = df[df['Quantity'] < 0 ].index
    df.drop(SuppQuantity , inplace=True)  #Efface quantité < 0

    SuppPrix = df[df["UnitPrice"]== 0].index
    df.drop(SuppPrix , inplace=True)  #Efface prix unitaire = 0
    
    indexNames = df[df['StockCode'].str.match('^A-Za-z')==True].index
    df.drop(indexNames , inplace=True) #Efface stockcode composer de A-Z et a-z
    df.drop_duplicates(subset= ['InvoiceNo', 'StockCode'], inplace = True)
    #Efface les doublon commun de la colonne facture et produit

    ######################################################################### Table Product
    country = df
    country.drop_duplicates(['Country'],keep = 'first', inplace= True)
    country.columns = country.columns.str.lower()
    country = country['country']
    
    ######################################################################### Connexion db
    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']

    db_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(user=user, password=password,
    database_name=database_name)
    
    engine = sqlalchemy.create_engine(db_url, echo=False)
    ######################################################################### Envoie dans db
    country.to_sql("country",if_exists='append', con = engine, index=False)


def page_csv(request):
    
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        file1 = TextIOWrapper(file, encoding='unicode_escape', newline='')
        
        df = pd.read_csv(file1, encoding='unicode_escape')
        df1 = df.copy()
        df2 = df.copy()
        df3 = df.copy()
        df4 = df.copy()

        produit(df1)
        country(df2)
        invoiceno(df3)
        detailfacture(df4)
        return HttpResponse('Is good')
    else:
        form = UploadFileForm()
    return render(request, "import.html", {'form':form})
    

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
