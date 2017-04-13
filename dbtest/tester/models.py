from django.db import models

# Create your models here.


class ViewerProduct(models.Model):
    proNo = models.CharField('proNo', max_length=4, primary_key=True)
    proName = models.CharField('proName', max_length=20)
    price = models.IntegerField('price')

    class Meta:
        db_table = 'v_test'
        managed = False


class BuyItems(models.Model):
    userName = models.CharField(max_length=20)
    itemNo = models.CharField(max_length=4)
