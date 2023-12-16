from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email =models.EmailField(max_length=255,null=True)
    date_crreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    CATEGORY =(
        ('Indoor', 'I'),
        ('Outdoor', 'O'),
       
    ) 
    name = models.CharField(max_length=255, null=True)
    price = models.FloatField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True, choices=CATEGORY)
    description = models.CharField(max_length=255, null=True)
  
    tags = models.ManyToManyField(Tag)

    def __str__(self):
       return self.name
STATUS =(
    ('Pending','Pending'),
    ('out of delivery','out of delivery'),
    ('Delivered','Delivered'),

)



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product =  models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)
    status=models.CharField(max_length=255, choices=STATUS,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return self.product.name
