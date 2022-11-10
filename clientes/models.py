from gc import DEBUG_COLLECTABLE
from django.db import models
from django.conf import settings

# Create your models here.

def upload_to(instance, filename):
    return settings.MEDIA_ROOT + '/{0}/{1}'.format(instance.customer_dni, filename)

class Cliente(models.Model):
    customer_id= models.AutoField(primary_key= True)
    customer_name= models.TextField()
    customer_surname= models.TextField()
    customer_dni= models.TextField(db_column= 'customer_DNI')
    customer_type= models.CharField(max_length=9)
    dob= models.TextField(blank= True, null= True)
    branch_id= models.IntegerField()
    img_profile= models.ImageField(upload_to=upload_to)

    class Meta():
        db_table= "cliente"
        

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'