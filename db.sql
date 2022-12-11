CREATE TABLE Produit(
   IdProduit VARCHAR(50),
   StockCode VARCHAR(50),
   Description VARCHAR(50),
   PRIMARY KEY(IdProduit)
);

CREATE TABLE Country(
   IdCountry VARCHAR(50),
   CustomerID VARCHAR(50),
   NameCountry VARCHAR(50),
   PRIMARY KEY(IdCountry)
);

CREATE TABLE Facture(
   idFacture VARCHAR(50),
   InvoiceNo VARCHAR(50),
   InvoiceDate timestamp,
   IdCountry VARCHAR(50) NOT NULL,
   PRIMARY KEY(idFacture),
   FOREIGN KEY(IdCountry) REFERENCES Country(IdCountry)
);

CREATE TABLE appartenir(
   IdProduit VARCHAR(50),
   idFacture VARCHAR(50),
   UnitPrice NUMERIC(6,2),
   Quantity NUMERIC(6,2),
   PRIMARY KEY(IdProduit),
   FOREIGN KEY(IdProduit) REFERENCES Produit(IdProduit),
   FOREIGN KEY(idFacture) REFERENCES Facture(idFacture)
);






------------------------------------------------------------------ 2e version avec zone

  CREATE TABLE Produit(
   IdProduit VARCHAR(50),
   StockCode VARCHAR(50),
   Description VARCHAR(50),
   PRIMARY KEY(IdProduit)
);

CREATE TABLE Zone(
   idZone VARCHAR(50),
   NameZone VARCHAR(50),
   PRIMARY KEY(idZone)
);

CREATE TABLE Country(
   IdCountry VARCHAR(50),
   CustomerID VARCHAR(50),
   NameCountry VARCHAR(50),
   idZone VARCHAR(50),
   PRIMARY KEY(IdCountry),
   FOREIGN KEY(idZone) REFERENCES Zone(idZone)

);

CREATE TABLE Facture(
   idFacture VARCHAR(50),
   InvoiceNo VARCHAR(50),
   InvoiceDate timestamp,
   IdCountry VARCHAR(50) NOT NULL,
   PRIMARY KEY(idFacture),
   FOREIGN KEY(IdCountry) REFERENCES Country(IdCountry)
);

CREATE TABLE appartenir(
   IdProduit VARCHAR(50),
   idFacture VARCHAR(50),
   UnitPrice NUMERIC(6,2),
   Quantity NUMERIC(6,2),
   PRIMARY KEY(IdProduit),
   FOREIGN KEY(IdProduit) REFERENCES Produit(IdProduit),
   FOREIGN KEY(idFacture) REFERENCES Facture(idFacture)
);
-----------------------------------------
CREATE TABLE Invoice(
   InvoiceNo VARCHAR(50),
   StockCode VARCHAR(50),
   Quantity INT,
   Country VARCHAR(50),
   UnitPrice NUMERIC(6,2),
   PRIMARY KEY(InvoiceNo)
);
---------------------------------------------
CREATE TABLE Product(
   stockcode VARCHAR(50),
   Description VARCHAR(80),
   PRIMARY KEY(stockcode)
);

CREATE TABLE Country(
   idCountry SERIAL PRIMARY KEY
   country VARCHAR(50),
   zone_name VARCHAR(50),
   
   
);

CREATE TABLE Invoice(
   invoice_no VARCHAR(6),
   invoice_date TIMESTAMP,
   country_name VARCHAR(50) NOT NULL,
   customer_id VARCHAR(5), 
   PRIMARY KEY(invoice_no),
   FOREIGN KEY(country_name) REFERENCES Country(country_name)
);

CREATE TABLE DetailFacture(
   stock_code VARCHAR(50),
   invoice_no VARCHAR(6),
   unit_price NUMERIC(6,2),
   quantity INT,
   detailfacture_id SERIAL PRIMARY KEY,
   FOREIGN KEY(stock_code) REFERENCES Product(stock_code),
   FOREIGN KEY(invoice_no) REFERENCES Invoice(invoice_no)
);

----------------------

CREATE TABLE country(
   country_id SERIAL PRIMARY KEY
   namecountry VARCHAR(50)
);

CREATE TABLE facture(
   idfacture SERIAL PRIMARY KEY,
   invoiceno VARCHAR(50) NOT NULL,
   stockcode VARCHAR(50),
   invoicedate TIMESTAMP,
   country_id VARCHAR(50),
   FOREIGN KEY(country_id) REFERENCES country(country_id)
);

