from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50, default=NULL)
    category=models.CharField(max_length=50,default=NULL)
    subcategory=models.CharField(max_length=50,default=NULL)
    desc=models.CharField(max_length=300, default=NULL)
    pub_date=models.DateField()
    image = models.ImageField(upload_to='shop/image', default=NULL)
    
    def _str_(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def _str_(self):
        return self.name
class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=12, default="")
    
class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)
def _str_(self):
    return self.update_desc[0:7] + "..."