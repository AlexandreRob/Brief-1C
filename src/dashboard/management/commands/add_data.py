from django.core.management.base import BaseCommand
import pandas as pd
from dashboard.models import Invoice
import sqlalchemy
from django.conf import settings

class Command(BaseCommand):


    def handle(self, *args , **options ):
        file_csv = "D:\Documents\Afpar exo\data2011s2.csv"
        df = df = pd.read_csv(file_csv, encoding= 'unicode_escape')
        country = df
        facture = df

        
        indexNames = country[country["Country"] == "Unspecified"].index
        country.drop(indexNames , inplace=True) #Efface les pays = a Unspecified
        
        facture = facture.drop(['Country', 'Description','Quantity','CustomerID','UnitPrice','InvoiceDate'], axis=1)
        indexNames = facture[facture['StockCode'].str.match('^A-Za-z')==True].index
        facture.drop(indexNames , inplace=True) #Efface les pays = a Unspecified
        facture.drop_duplicates(subset= ['InvoiceNo', 'StockCode'], inplace = True)
        #Efface les doublon commun de la colonne facture et produit

        facture.columns = facture.columns.str.lower()
        country.columns = country.columns.str.lower()
        country = country['country']
        
        
        
        # engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost/DB_AFPAR01')
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']

        db_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(user=user, password=password,
        database_name=database_name)
        
        engine = sqlalchemy.create_engine(db_url, echo=False)
        
        facture.to_sql("facture",if_exists='append', con = engine, index=False)
        country.to_sql("country",if_exists='append', con = engine, index=False)
