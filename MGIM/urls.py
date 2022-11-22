from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_gate_inventory_manager, name='main-gate-inventory-manager'),
    path('inventory/', views.inventory, name='MGIM-inventory'),
    path('entry-details/', views.entry_details, name='entry-details'),
    path('entry-details-next/<str:RegNo>', views.entry_details_next, name='entry-details-next'),
    path('exit-details/', views.exit_details, name='exit-details'),
]
