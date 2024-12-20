from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import generics
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
        if serializer.is_valid:
            
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)



class view_items(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    def get(self):
        items=item.objects.all()
        serializer=itemserialization(items,many=True)
        if serializer.is_valid:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
        
        
        
class view_speciefic_item(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self):
        speciefic_item=get_object_or_404(item,pk=id)
        serializer=itemserialization(speciefic_item)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)