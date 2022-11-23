import pandas as pd

df = pd.read_csv('data.csv', encoding= 'unicode_escape')

df = df.dropna(axis=0) #Efface les null dans le tableau
df = df.drop(['StockCode', 'Description', 'InvoiceDate'], axis=1) # Efface des colonne dans le tableau

print(df.head(10))


