from django.urls import path
from .views import *
from rest_framework.authtoken import views
urlpatterns = [
    path('api-token/',views.obtain_auth_token),
    path('view_inventorys/',view_inventorys.as_view(),name="view_inventorys"),
    path('view_items/',view_items.as_view(),name="view_items"),
    path('view_speciefic_item/<int:id>/',view_speciefic_item.as_view(),name="view_speciefic_item"),
    path('add_items/',add_items.as_view(),name="add_items"),
    path('add_inventorys/',add_inventorys.as_view(),name="add_inventorys"),
    path('delete_items/',delete_items.as_view(),name="delete_items"),
    path('delete_inventorys/',delete_inventorys.as_view(),name="delete_inventorys"),
    path('delete_speciefic_item/',delete_speciefic_item.as_view(),name="delete_speciefic_item"),
    path('delete_speciefic_invetory/',delete_speciefic_invetory.as_view(),name="delete_speciefic_invetory"),

]
