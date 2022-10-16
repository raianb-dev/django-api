from uuid import uuid4
from django.db import models

class users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    balance = models.DecimalField(max_digits=9,decimal_places=True )
    bank_name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)  
    
class movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)