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