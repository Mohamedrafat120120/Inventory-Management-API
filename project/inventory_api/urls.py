from django.urls import path
from .views import *
urlpatterns = [
    path('view_inventorys/',view_inventorys.as_view(),name="view_inventorys"),
    path('view_items/',view_items.as_view(),name="view_items"),
    path('view_speciefic_item/<int:id>/',view_speciefic_item.as_view(),name="view_speciefic_item"),
    path('add_item/',add_item.as_view(),name="add_items"),
    path('add_inventory/',add_inventory.as_view(),name="add_inventorys"),
    path('delete_items/',delete_items.as_view(),name="delete_items"),
    path('delete_inventorys/',delete_inventorys.as_view(),name="delete_inventorys"),
    path('delete_speciefic_item/<int:id>/',delete_speciefic_item.as_view(),name="delete_speciefic_item"),
    path('delete_speciefic_invetory/<int:id>/',delete_speciefic_invetory.as_view(),name="delete_speciefic_invetory"),
    path('update_item/<int:id>/',update_item.as_view(),name="update_item"),
    path('update_inventory/<int:id>/',update_inventory.as_view(),name="update_inventory"),
    path('filter_items/<str:category>/',filter_items.as_view(),name='filter_items'),
    path('sort_items/<str:name>/',sort_items.as_view(),name='sort_items')

]
