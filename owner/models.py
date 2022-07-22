from django.db import models

# Create your models here.
class Owner(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    itemname=models.CharField(max_length=100,default="")
    itemprice=models.CharField(max_length=100,default="")
    image=models.FileField(upload_to='static/images/items', default='default.jpg')

    class Meta:
        db_table="owner"