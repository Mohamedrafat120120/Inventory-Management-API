from django.shortcuts import get_object_or_404
from .models import item,inventory
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class view_inventorys(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    def get(self,request):
        inventorys=inventory.objects.all()
        serializer=inventoryserialization(inventorys,many=True)
            
        return Response(serializer.data,status=status.HTTP_200_OK)



class view_items(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    def get(self,request):
        items=item.objects.all()
        serializer=itemserialization(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
        
        
class view_speciefic_item(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    def get(self,request,id):
        speciefic_item=get_object_or_404(item,pk=id)
        serializer=itemserialization(speciefic_item)
        return Response(serializer.data,status=status.HTTP_200_OK)
