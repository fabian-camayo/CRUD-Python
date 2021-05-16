from django.db import models
from django.utils import timezone
 
class Menus(models.Model):
    name = models.CharField(max_length=100, default='DEFAULT VALUE')
    price = models.CharField(max_length=20, default='DEFAULT VALUE')
    stock = models.CharField(max_length=100, default='DEFAULT VALUE')
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
         db_table = 'menus'