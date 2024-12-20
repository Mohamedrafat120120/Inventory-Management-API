from django.urls import path
from .views import *
urlpatterns = [
    path('view_inventorys/',view_inventorys.as_view(),name="view_inventorys"),
    path('view_items/',view_items.as_view(),name="view_items"),
    path('view_speciefic_item/<int:id>/',view_speciefic_item.as_view(),name="view_speciefic_item"),

]
