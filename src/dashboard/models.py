from django.db import models

class Appartenir(models.Model):
    stockcode = models.OneToOneField('Produit', models.DO_NOTHING, db_column='stockcode', primary_key=True)
    invoiceno = models.ForeignKey('Facture', models.DO_NOTHING, db_column='invoiceno', blank=True, null=True)
    unitprice = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appartenir'


class Country(models.Model):
    namecountry = models.CharField(primary_key=True, max_length=50)
    namezone = models.CharField(max_length=50, blank=True, null=True)
    idzone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='idzone')

    class Meta:
        managed = False
        db_table = 'country'


class Facture(models.Model):
    invoiceno = models.CharField(primary_key=True, max_length=50)
    invoicedate = models.DateTimeField(blank=True, null=True)
    namecountry = models.ForeignKey(Country, models.DO_NOTHING, db_column='namecountry')

    class Meta:
        managed = False
        db_table = 'facture'


class Produit(models.Model):
    stockcode = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'produit'


class Zone(models.Model):
    idzone = models.CharField(primary_key=True, max_length=50)
    namezone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zone'
