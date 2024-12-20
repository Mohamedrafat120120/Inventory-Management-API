from django.db import models
# Create your models here.
class item(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    description=models.CharField(max_length=100,null=False,blank=False)
    price=models.DecimalField(max_digits=4,decimal_places=3,null=False,blank=False)
    
    
    
    def __str__(self):
        return self.name
        
class inventory(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    location=models.CharField(max_length=100,null=False,blank=False)
    quantity=models.IntegerField()
    items=models.ForeignKey(item,on_delete=models.CASCADE,null=False,blank=False,default=None)
    
    def __str__(self):
        return self.name
        
        