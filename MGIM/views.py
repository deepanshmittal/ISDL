from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect

from myapp.models import *


# Create your views here.
def main_gate_inventory_manager(request):
    return redirect('MGIM-inventory')


def getRole(request):
    return Profile.objects.get(Owner=request.user).Role


@login_required(login_url='login')
def inventory(request):
    if getRole(request) == "MGIM":
        inventory = Inventory.objects.all()
        # print(len(inventory))
        return render(request, 'MGIM-inventory.html', {'inventory': inventory})
    else:
        return redirect('login')


@login_required(login_url='login')
def entry_details(request):
    if getRole(request) == "MGIM":
        purchase = Purchase.objects.filter(Status="Pending")
        if request.method == "POST":
            RegNo = request.POST.get('RegNo')
            return redirect(f'/main-gate-inventory-manager/entry-details-next/{RegNo}')
        return render(request, 'MGIM-entry-details.html', {'purchase': purchase})
    else:
        return redirect('login')


@login_required(login_url='login')
def entry_details_next(request, RegNo):
    if getRole(request) == "MGIM":
        itemList = ItemList.objects.filter(Bill__RegNo=RegNo, Quantity__gt=0)
        if request.method == 'POST':
            Delivered_Quantity = list(map(int, dict(request.POST).get('Delivered_Quantity')))
            try:
                with transaction.atomic():
                    cnt = 0
                    print(itemList)
                    for Quantity, item in zip(Delivered_Quantity, itemList):
                        item.Quantity -= Quantity
                        i = item.ItemCode
                        i.Quantity += Quantity
                        i.save()
                        item.save()
                        if item.Quantity == 0:
                            cnt += 1
                    print(cnt, len(itemList))
                    if cnt == len(itemList):
                        purchase = Purchase.objects.get(Bill__RegNo=RegNo)
                        purchase.Status = 'Complete'
                        purchase.save()
                        messages.success(request, "Order Completely Delivered.")
                        return redirect('entry-details')
                    messages.success(request, "Records updated Successfully.")
                    return redirect('entry-details')
            except:
                messages.error(request, "Some error occurred while updating the records.")
                return redirect(f'/main-gate-inventory-manager/entry-details-next/{RegNo}')
        return render(request, 'MGIM-entry-details-next.html', {'RegNo': RegNo, 'itemList': itemList})
    else:
        return redirect('login')


@login_required(login_url='login')
def exit_details(request):
    if getRole(request) == "MGIM":
        items = Item.objects.filter(Quantity__gt=0)
        if request.method == 'POST':
            data = request.POST
            ItemCode = data.get('ItemCode')
            Quantity = int(data.get('Quantity'))
            # print(ItemCode, Quantity)
            try:
                with transaction.atomic():
                    Item_object = Item.objects.get(ItemCode=ItemCode)
                    Item_object.Quantity -= Quantity
                    Item_object.save()
                    messages.success(request, "Item Removed Successfully")
                    return redirect('exit-details')
            except:
                messages.error(request, "Some Error Occured !")
                return redirect('exit-details')
        return render(request, 'MGIM-exit-details.html', {'items': items})
    else:
        return redirect('login')
