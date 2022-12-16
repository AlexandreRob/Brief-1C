from django.core.management.base import BaseCommand
import pandas as pd
import sqlalchemy
from django.conf import settings
from dashboard.models import Product

class Command(BaseCommand):


    def handle(self, *args , **options ):
        file_csv = "D:\Documents\Afpar exo\Brief-1C\data2011s2.csv"
        df = df = pd.read_csv(file_csv, encoding= 'unicode_escape')

        ######################################################################### Nettoyage df
        df
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
        dfPropre = df.copy()
        

        ######################################################################### Table Product
        product = dfPropre
        product = product.drop(['Country','InvoiceNo','UnitPrice','Quantity','CustomerID','InvoiceDate'], axis=1)
        product.drop_duplicates("StockCode", keep = 'first', inplace= True)
        
        
        ######################################################################### Table detailfacture
        detailfacture = dfPropre
        detailfacture = detailfacture.drop(['Country', 'Description','CustomerID','InvoiceDate'], axis=1)
        
        

        ######################################################################### Table InvoiceNo
        invoiceno = dfPropre
        invoiceno = invoiceno.drop(['Description','Quantity','UnitPrice','Description','StockCode','InvoiceDate','CustomerID'], axis=1)
        invoiceno.drop_duplicates("InvoiceNo", keep = 'first', inplace= True)

        product.columns = product.columns.str.lower()
        invoiceno.columns = invoiceno.columns.str.lower()
        detailfacture.columns = detailfacture.columns.str.lower()

        ######################################################################### Table Country
        country = dfPropre
        country.drop_duplicates(['Country'],keep = 'first', inplace= True)
        country.columns = country.columns.str.lower()
        country = country['country']
        
        
        
        # engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost/DB_AFPAR01')
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']

        db_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(user=user, password=password,
        database_name=database_name)
        
        engine = sqlalchemy.create_engine(db_url, echo=False)
        





        row_iter = product.iterrows()

        objs = [

            Product(

                stockcode = row['stockcode'],

                description = row['description'],
            )

            for index, row in row_iter

        ]

        Product.objects.bulk_create(objs)

        
        country.to_sql("country",if_exists='append', con = engine, index=False)
        invoiceno.to_sql('invoice',if_exists='append', con = engine, index=False)
        detailfacture.to_sql("detailfacture",if_exists='append', con = engine, index=False)
