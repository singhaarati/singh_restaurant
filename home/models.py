from django.db import models

# Create your models here.
class Buy(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    mobile=models.CharField(max_length=150)
    address=models.CharField(max_length=200,default="")
    zipcode=models.CharField(max_length=20)

    class Meta:
        db_table="buy"
