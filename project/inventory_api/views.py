from django.shortcuts import get_object_or_404
from .models import item,inventory
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,generics,filters
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


class add_item(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def post(self,request):
        serializer=itemserialization(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class add_inventory(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def post(self,request):
        if not inventory.objects.filter(name=request.data['name']).exists():
           serializer=inventoryserialization(data=request.data)
           if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data,status=status.HTTP_201_CREATED)
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({"error":"inventory name already exists"},status=status.HTTP_400_BAD_REQUEST)
    
class delete_items(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def delete(self,request):
       items=item.objects.all()
       if items:
           items.delete()
           return Response({"message":"items deleted"},status=status.HTTP_200_OK)
       return Response({"message":"no items to delete"},status=status.HTTP_400_BAD_REQUEST)
   
   
class delete_inventorys(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def delete(self,request):
       inventorys=inventory.objects.all()
       if inventorys:
           inventorys.delete()
           return Response({"message":"inventorys deleted"},status=status.HTTP_200_OK)
       return Response({"message":"no inventorys to delete"},status=status.HTTP_400_BAD_REQUEST)
   
class delete_speciefic_item(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def delete(self,request,id):
       Item=get_object_or_404(item,PK=id)
       if Item:
           Item.delete()
           return Response({"message":"item deleted"},status=status.HTTP_200_OK)
       return Response({"message":"no items to delete"},status=status.HTTP_400_BAD_REQUEST)
   
class delete_speciefic_invetory(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def delete(self,request,id):
       Inventory=get_object_or_404(inventory,pk=id)
       if Inventory:
           Inventory.delete()
           return Response({"message":"inventory deleted"},status=status.HTTP_200_OK)
       return Response({"message":"no inventorys to delete"},status=status.HTTP_400_BAD_REQUEST)
   
   
class update_item(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def put(self,request,id):
        Item=get_object_or_404(item,pk=id)
        # Item.name=request.data['name']
        # Item.description=request.data['description']
        # Item.quantity=request.data['quantity']
        # Item.category=request.data['category']
        # Item.price=request.data['price']
        # Item.save()
        serialize=itemserialization(Item,request.data)
        return Response({"message":"item updated","Data":serialize.data},status=status.HTTP_200_OK)
        
class update_inventory(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def put(self,request,id):
        Inventory=get_object_or_404(inventory,pk=id)
        # Inventory.name=request.data['name']
        # Inventory.location=request.data['location']
        # Inventory.items_quantity=request.data['items_quantity']
        # Inventory.category=request.data['category']
        # Inventory.save()
        serialize=inventoryserialization(Inventory,request.data)
        return Response({"message":"item updated","Data":serialize.data},status=status.HTTP_200_OK)   
       
           
           
class filter_items(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=itemserialization
    def get_queryset(self):
        category=self.kwargs.get('category')
        return item.objects.filter(category=category)
        
        
        
class sort_items(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset=item.objects.all()
    serializer_class=itemserialization
    filter_backends=[filters.OrderingFilter]
    ordering_fields=['name','price']
    
    

    