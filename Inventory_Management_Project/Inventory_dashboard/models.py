from django.db import models


CATEGORY = (
    ('Meat' , 'Meat'),
    ('Dessert' , 'Dessert'),
    ('Vegetable' , 'Vegetable'),
    ('Sauces' , 'Sauces'),
    ('Fruit' , 'Fruit'),
    )
class Product(models.Model):
    name=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=20,choices=CATEGORY,null=True)
    quantity=models.PositiveIntegerField(null=True)
    expirydate =models.DateField(null=True) 

    objects = models.Manager()

# Create your models here.

    def __str__(self):
      return f'{self.name}-{self.quantity}'
      
class Order(models.Model):
    name = models.CharField(max_length=100,null=True)
    quantity = models.PositiveIntegerField(null=True)
    category=models.CharField(max_length=20,choices=CATEGORY,null=True)
    
    objects = models.Manager()
    


    def __str__(self):
        return f'{self.name}-{self.quantity}'