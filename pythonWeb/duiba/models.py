from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=20)
    ages = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'test'
        
        
        
class User(models.Model):
    name = models.CharField(max_length=20)
    credits = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'user'


class Quwei(models.Model):
    titles = models.CharField(max_length=100)
    contents = models.CharField(max_length=200)
    links = models.CharField(max_length=100)
    images = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    times = models.CharField(max_length=100)
    class Meta:
        db_table = 'quwei'




