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
