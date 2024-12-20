from rest_framework import serializers
from .models import *
class itemserialization(serializers.ModelSerializer):
    
    class Meta:
        model = item
        fields =['id','name','description','price']
class inventoryserialization(serializers.ModelSerializer):
    item=itemserialization(many=True,read_only=True)
    class Meta:
        model = inventory
        fields='__all__'