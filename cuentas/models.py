from distutils.sysconfig import customize_compiler
from msilib.schema import Class
from django.db import models
from clientes.models import Cliente

# Create your models here.

class Cuenta(models.Model):
    account_id= models.AutoField(primary_key= True)
    customer= models.ForeignKey(Cliente, on_delete= models.CASCADE)
    balance= models.IntegerField()
    iban= models.TextField()

    class Meta():
        db_table= "cuenta"

