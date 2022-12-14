from django.core.management.base import BaseCommand
import pandas as pd
import sqlalchemy
from django.conf import settings
from dashboard.models import Product

class Command(BaseCommand):


    def handle(self, *args , **options ):
        # engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost/DB_AFPAR01')
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']

        db_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(user=user, password=password,
        database_name=database_name)
        
        engine = sqlalchemy.create_engine(db_url, echo=False)
        
        df = pd.read_sql('''SELECT I.invoiceno, D.stockcode, country
                        FROM invoice as I 
                        INNER JOIN detailfacture as D on I.invoiceno = D.invoiceno
                        GROUP BY I.invoiceno,D.stockcode''', con=engine)

        df.groupby(['country', 'stockcode']).sum().sort_values(['country'], ascending=True).groupby('country').head(2)
        df = df.to_dict()
        print(df)



        
        
