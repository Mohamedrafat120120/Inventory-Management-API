from django.db import models
# Create your models here.

class category(models.TextChoices):
    ELECTRONICS='ELECTRONICS',
    FASHION='FASHION',
    HOME_APPLIANCES='HOME_APPLIANCES',
    WOOD='WOOD',
    FURNITURES='FURNITURES',
    SPORTS='SPORTS',
    BOOKS='BOOKS',
    TOYS='TOYS',
    ELECTRONICS_ACCESSORIES='ELECTRONICS_ACCESSORIES',
    PHONES='PHONES',
    SMART_DEVICES='SMART_DEVICES',
    IRONS='IRONS'
class item(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    description=models.CharField(max_length=100)
    quantity=models.IntegerField(null=False,blank=False,default=None)
    category=models.CharField(max_length=100,choices=category.choices,null=False,blank=False)
    price=models.DecimalField(max_digits=4,decimal_places=3,null=False,blank=False)
    date_add=models.DateField(auto_now_add=True)
    last_updated=models.DateField(auto_now=True)
    
    
    
    def __str__(self):
        return self.name
        
class inventory(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    location=models.CharField(max_length=100,null=False,blank=False)
    items_quantity=models.IntegerField()
    category=models.CharField(max_length=100,choices=category.choices,null=False,blank=False,default=None)
    date_add=models.DateField(auto_now_add=True)
    items=models.ForeignKey(item,on_delete=models.PROTECT,null=False,blank=False)
    last_updated=models.DateField(auto_now=True)

    
    def __str__(self):
        return self.name
        
        