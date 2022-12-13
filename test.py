import pandas as pd
import sqlalchemy
import psycopg2
import psycopg2.extras as extras

df = pd.read_csv('data.csv', encoding= 'unicode_escape')

############################################################### nettoyer les données brutes (suppression des doublons et “faux”, standardisation, etc)
df = df.drop(['CustomerID', 'InvoiceDate','Description'], axis=1) 
#Ne pas oublier axis= 0 pour les lignes 1 pour les colonnes
#Efface du tableau les colonnes CustomerID InvoiceDate et Description

df.duplicated().sum() #nombre de doublon #La méthode duplicated() renvoie une valeur booléenne pour chaque ligne

df.drop_duplicates(inplace= True) #efface les doublons
############################################################### 

############################################################### 
#un graphique précisant la répartition des ventes par produit


# ################################ Nettoyage du csv commande 

SuppQuantity = df[ df['Quantity'] < 0 ].index
df.drop(SuppQuantity , inplace=True)  #Efface quantité < 0

SuppPrix = df[df["UnitPrice"]== 0].index
df.drop(SuppPrix , inplace=True)  #Efface prix unitaire = 0

SuppPunsp = df[df["Country"] == "Unspecified"].index
df.drop(SuppPunsp , inplace=True) #Efface les pays = a Unspecified

df.drop_duplicates(subset= ['InvoiceNo', 'StockCode'], inplace = True)
print(df) #Efface les doublon commun de la colonne facture et produit

# Plus que 236033 ligne normalement sur 245903

# Execution du code valeur correct 





def execute_values(request,conn, df, table):
    if request.method == "POST":
        nom_fichier = request.POST["csv"]

        tuples = [tuple(x) for x in df.to_numpy()]
    
        cols = ','.join(list(df.columns))
    
        # SQL query to execute
        query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
        cursor = conn.cursor()
        try:
            extras.execute_values(cursor, query, tuples)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            conn.rollback()
            cursor.close()
            return 1
        print("execute_values() done")
        cursor.close()
  
  
# establishing connection
conn = psycopg2.connect(
    database="Airlines_Database",
    user='postgres',
    password='sherlockedisi',
    host='127.0.0.1',
    port='5432'
)
sql = '''CREATE TABLE airlines_final1(id int ,day
char(20) ,airline char(20),destination char(20));'''
  
# creating a cursor
cursor = conn.cursor()
cursor.execute(sql)
data = pd.read_csv("airlines_final.csv")
  
data = data[["id", "day", "airline", "destination"]]
  
# using the function defined
execute_values(conn, data, 'airlines_final1')
# CREATE TABLE airlines_final1(id int ,day char(20) ,airline char(20),destination char(20));

engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost/DB_AFPAR01')

df = pd.read_csv('D:\Documents/Afpar exo/Brief-1C/data.csv', encoding= 'unicode_escape')

df.to_sql('country', engine, if_exists="append", index=False)





# ###########################################
SuppQuantity = df[df['Quantity'] < 0 ].index
df.drop(SuppQuantity , inplace=True)  #Efface quantité < 0

SuppPrix = df[df["UnitPrice"]== 0].index
df.drop(SuppPrix , inplace=True)  #Efface prix unitaire = 0

SuppPunsp = df[df["Country"] == "Unspecified"].index
df.drop(SuppPunsp , inplace=True) #Efface les pays = a Unspecified

df.drop_duplicates(subset= ['InvoiceNo', 'StockCode'], inplace = True)

df = df.drop(["InvoiceDate","CustomerID","Country","InvoiceNo","InvoiceDate","Quantity","UnitPrice"], axis=1)
df.columns = df.columns.str.lower()
df["stockcode"] = df["stockcode"].str.lower()

df = df.drop_duplicates(subset=["stockcode"], inplace=True)

df.columns = df.columns.str.lower()