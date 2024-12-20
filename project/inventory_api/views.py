from django.shortcuts import get_object_or_404
from .models import item,inventory
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class view_inventorys(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request):
        inventorys=inventory.objects.all()
        serializer=inventoryserialization(inventorys,many=True)
            
        return Response(serializer.data,status=status.HTTP_200_OK)



class view_items(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request):
        items=item.objects.all()
        serializer=itemserialization(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
        
        
class view_speciefic_item(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request,id):
        speciefic_item=get_object_or_404(item,pk=id)
        serializer=itemserialization(speciefic_item)
        return Response(serializer.data,status=status.HTTP_200_OK)


class add_items(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    def post(self,request):
        serializer=itemserialization(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class add_inventorys(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    def post(self,request):
        
        serializer=inventoryserialization(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class delete_items(APIView):
    def get(self,request):
       items=item.objects.all()
       if items:
           items.delete()
           return Response({"message":"items deleted"},status=status.HTTP_200_OK)
       return Response({"message":"no items to delete"},status=status.HTTP_400_BAD_REQUEST)
   
   
class delete_inventorys(APIView):
    def get(self,request):
       inventorys=inventory.objects.all()
       if inventorys:
           inventorys.delete()
           return Response({"message":"inventorys deleted"},status=status.HTTP_200_OK)
       return Response({"message":"no inventorys to delete"},status=status.HTTP_400_BAD_REQUEST)
   
class delete_speciefic_item(APIView):
    def get(self,request,id):
       item=get_object_or_404(item,pk=id)
       if item:
           item.delete()
           return Response({"message":"item deleted"},status=status.HTTP_200_OK)
       return Response({"message":"no items to delete"},status=status.HTTP_400_BAD_REQUEST)
   
class delete_speciefic_invetory(APIView):
    def get(self,request,id):
       inventory=get_object_or_404(inventory,pk=id)
       if inventory:
           inventory.delete()
           return Response({"message":"inventory deleted"},status=status.HTTP_200_OK)
       return Response({"message":"no inventorys to delete"},status=status.HTTP_400_BAD_REQUEST)
   
   
   
       
           