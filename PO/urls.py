from django.urls import path

from . import views

urlpatterns = [
    path('', views.purchase_officer, name='purchase-officer'),
    path('inventory/', views.inventory, name='PO-inventory'),
    path('pending-request/', views.pending_request, name='pending-request'),
    path('pending-request/show-quotation/<str:RegNo>', views.pending_request_show_quotation,
         name='pending-request-show-quotation'),
    path('request-history/', views.request_history, name='request-history'),
]
