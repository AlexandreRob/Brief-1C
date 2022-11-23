import pandas as pd

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
