from rest_framework import serializers
from .models import *
class itemserialization(serializers.ModelSerializer):
    class Meta:
        model = item
        fields ='__all__'
class inventoryserialization(serializers.ModelSerializer):
    item=itemserialization(many=True,read_only=True)
    class Meta:
        model = inventory
        fields='__all__'