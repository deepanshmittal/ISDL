import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect

from myapp.models import *


# Create your views here.
def inventory_manager(request):
    return redirect('IM-inventory')


def getRole(request):
    return Profile.objects.get(Owner=request.user).Role


@login_required(login_url='login')
def inventory(request):
    if getRole(request) == "IM":
        inventory = Inventory.objects.all()
        q = request.GET.get('q') if request.GET.get('q') is not None else ''
        print(q)
        if q:
            option = request.GET.get('option')
            print(option)
            if option == 'BuildingID':
                inventory = inventory.filter(BuildingID=q)
            elif option == 'Floor':
                inventory = inventory.filter(Floor=int(q))
            elif option == 'Room':
                inventory = inventory.filter(Room=q)
            elif option == 'ItemCode':
                inventory = inventory.filter(ItemCode__ItemCode=q)
            elif option == 'ItemNumber':
                inventory = inventory.filter(ItemNumber=int(q))
            elif option == 'Name':
                inventory = inventory.filter(ItemCode__Name__icontains=q)

        return render(request, 'IM-inventory.html', {'inventory': inventory})
    else:
        return redirect('login')


@login_required(login_url='login')
def add_inventory(request):
    if getRole(request) == "IM":
        items = Item.objects.filter(Quantity__gt=0)
        if request.method == 'POST':
            data = request.POST
            ItemCode = data.get('ItemCode').upper()
            BuildingID = data.get('BuildingID').upper()
            Floor = data.get('Floor')
            Room = data.get('Room').upper()
            # print([ItemCode, BuildingID, Floor, Room])
            try:
                with transaction.atomic():
                    item = Item.objects.get(ItemCode=ItemCode)
                    inventory_obj = Inventory(BuildingID=BuildingID, ItemCode=item, Floor=Floor, Room=Room)
                    inventory_obj.save()
                    item.Quantity -= 1
                    item.save()
                    CODE = f'LNM|{inventory_obj.BuildingID}|{inventory_obj.Floor}|{inventory_obj.Room}|{ItemCode}|{inventory_obj.ItemNumber}'
                    # print(CODE)
                    messages.success(request, f"Successfully Added: {CODE}")
                    return redirect('add-inventory')
            except:
                messages.error(request, "Some Error Occurred !")
        return render(request, 'IM-add-inventory.html', {'items': items})
    else:
        return redirect('login')


@login_required(login_url='login')
def remove_inventory(request):
    if getRole(request) == "IM":
        if request.method == "POST":
            ItemCode = request.POST.get('ItemCode')
            ItemNumber = request.POST.get('ItemNum')
            try:
                with transaction.atomic():
                    item_object = Item.objects.get(ItemCode=ItemCode)
                    Inventory.objects.get(ItemCode=item_object, ItemNumber=ItemNumber).delete()
                    item_object.Quantity += 1
                    item_object.save()
                    messages.success(request, "Item Successfully removed from Inventory")
            except:
                messages.error(request, "Some Error occurred !")
        return render(request, 'IM-remove-inventory.html')
    else:
        return redirect('login')


@login_required(login_url='login')
def register_item(request):
    if getRole(request) == "IM":
        items = Item.objects.all()
        if request.method == 'POST':
            data = request.POST
            ItemName = data.get('ItemName')
            ItemCode = data.get('ItemCode')
            try:
                with transaction.atomic():
                    item = Item(ItemCode=ItemCode, Name=ItemName)
                    item.save()
                    messages.success(request, "Item Added Successfully")
                    return redirect('register-item')
            except:
                messages.error(request, "Some Error Occured !")
                return redirect('register-item')
        return render(request, 'IM-register-item.html', {'items': items})
    else:
        return redirect('login')


@login_required(login_url='login')
def request_purchase(request):
    if getRole(request) == "IM":
        if request.method == 'POST':
            if request.POST.get('Add to List'):
                # print("add to list")
                itemList = request.POST.get('itemList')
                ItemCode = request.POST.get('ItemCode')
                Quantity = request.POST.get('Quantity')
                if not itemList:
                    itemList = '{}'

                itemList = json.loads(itemList.replace("'", '"'))  # JSON, dictionary of python
                try:
                    if Item.objects.get(ItemCode=ItemCode) and Quantity.isnumeric() and int(Quantity) > 0:
                        itemList[ItemCode] = itemList.get(ItemCode, 0) + int(Quantity)
                except Item.DoesNotExist:
                    messages.error(request, "Item does not exist")

                return render(request, 'IM-request-purchase.html', {'itemList': itemList})
            elif request.POST.get('Proceed'):
                # print("proceed")
                itemList = request.POST.get('itemList')
                if not itemList or itemList == '{}':
                    messages.error(request, "No Items added to List")
                    return redirect('request-purchase')

                itemList = json.loads(itemList.replace("'", '"'))
                try:
                    with transaction.atomic():
                        bill = Bill()
                        bill.save()
                        # print(itemList)
                        for (ItemCode, Quantity) in itemList.items():
                            # print(ItemCode, Quantity, sep=":")
                            ItemList(Bill=bill, ItemCode=Item.objects.get(ItemCode=ItemCode), Quantity=Quantity).save()
                        messages.info(request, f"{bill.RegNo}")
                        return redirect('request-purchase-quotations')
                except:
                    messages.error(request, "Some Error Occurred! Please Try Again")
                    return render(request, 'IM-request-purchase.html', {'itemList': itemList})

        return render(request, 'IM-request-purchase.html')
    else:
        return redirect('login')


@login_required(login_url='login')
def request_purchase_quotations(request):
    if getRole(request) == "IM":
        if request.method == 'POST':
            data = request.POST
            RegNo = data.get('RegNo')
            Quotations = dict()
            Quotations['Quotation1'] = {'Quotee': data.get('Quotee1'), 'Amount': data.get('Amount1'),
                                        'Link': data.get('QuotationLink1')}
            Quotations['Quotation2'] = {'Quotee': data.get('Quotee2'), 'Amount': data.get('Amount2'),
                                        'Link': data.get('QuotationLink2')}
            Quotations['Quotation3'] = {'Quotee': data.get('Quotee3'), 'Amount': data.get('Amount3'),
                                        'Link': data.get('QuotationLink3')}
            print(Quotations)
            try:
                with transaction.atomic():
                    for quotation in Quotations.values():
                        print(quotation.values())
                        if all(x == '' for x in quotation.values()):
                            continue
                        elif any(x == '' for x in quotation.values()):
                            raise Exception()
                        else:
                            Quotation(Bill=Bill.objects.get(RegNo=RegNo), QuotationLink=quotation['Link'],
                                      Quotee=quotation['Quotee'], Amount=quotation['Amount']).save()

                messages.success(request, "Quotations Successfully sent for Approval")
            except:
                messages.error(request, "Incorrect Entries!")
                messages.info(request, RegNo)
                return redirect('request-purchase-quotations')

            return redirect('request-purchase')

        return render(request, 'IM-request-purchase-quotations.html')
    else:
        return redirect('login')
