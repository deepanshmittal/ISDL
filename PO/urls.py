from django.urls import path

from . import views

urlpatterns = [
    path('', views.purchase_officer, name='purchase-officer'),
    path('inventory/', views.inventory, name='PO-inventory'),
    path('request-history/', views.request_history, name='request-history'),
    path('pending-request/', views.pending_request, name='pending-request'),
]
