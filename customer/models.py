from django.db import models

# Create your models here.
class Customer(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    firstname=models.CharField(max_length=100,default="")
    lastname=models.CharField(max_length=100,default="")
    username=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=150,default="")
    mobile=models.CharField(max_length=150,default="")
    address=models.CharField(max_length=200,default="")
    zipcode=models.CharField(max_length=20,default="")
    # image=models.FileField(upload_to='static/images/customer', default='default.jpg')

    class Meta:
        db_table="customer" 