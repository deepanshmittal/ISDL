from django.urls import path

from . import views

urlpatterns = [
    path('', views.inventory_manager, name='inventory-manager'),
    path('inventory/', views.inventory, name='IM-inventory'),
    path('remove-inventory/', views.remove_inventory, name='remove-inventory'),
    path('request-purchase/', views.request_purchase, name='request-purchase'),
    path('request-purchase/quotations', views.request_purchase_quotations, name='request-purchase-quotations'),
    path('add-inventory/', views.add_inventory, name='add-inventory'),
    path('register-item/', views.register_item, name='register-item'),
]
