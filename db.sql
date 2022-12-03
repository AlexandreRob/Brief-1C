CREATE TABLE Produit(
   StockCode VARCHAR(50),
   PRIMARY KEY(StockCode)
);

CREATE TABLE Zone(
   idZone VARCHAR(50),
   nameZone VARCHAR(50),
   PRIMARY KEY(idZone)
);

CREATE TABLE Country(
   NameCountry VARCHAR(50),
   nameZone VARCHAR(50),
   idZone VARCHAR(50) NOT NULL,
   PRIMARY KEY(NameCountry),
   FOREIGN KEY(idZone) REFERENCES Zone(idZone)
);

CREATE TABLE Facture(
   InvoiceNo VARCHAR(50),
   InvoiceDate DATETIME,
   NameCountry VARCHAR(50) NOT NULL,
   PRIMARY KEY(InvoiceNo),
   FOREIGN KEY(NameCountry) REFERENCES Country(NameCountry)
);

CREATE TABLE Appartenir(
   StockCode VARCHAR(50),
   InvoiceNo VARCHAR(50),
   UnitPrice NUMERIC(6,2),
   Quantity INT,
   PRIMARY KEY(StockCode),
   FOREIGN KEY(StockCode) REFERENCES Produit(StockCode),
   FOREIGN KEY(InvoiceNo) REFERENCES Facture(InvoiceNo)
);





------------------------------------------------------------------ 2e version

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
   PRIMARY KEY(idFacture)
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

CREATE TABLE Avoir(
   IdCountry VARCHAR(50),
   idFacture VARCHAR(50),
   PRIMARY KEY(IdCountry),
   FOREIGN KEY(IdCountry) REFERENCES Country(IdCountry),
   FOREIGN KEY(idFacture) REFERENCES Facture(idFacture)
);