from rest_framework import serializers
from .models import MyUser
class register_serializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields='__all__'
        
        
class login_serializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=['email','password']
        
        
class profile_serializer(serializers.ModelField):
    class Meta:
        model=MyUser
        fields='__all__'