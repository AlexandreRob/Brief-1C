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
