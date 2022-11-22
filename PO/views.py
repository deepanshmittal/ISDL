from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect

from myapp.models import *


# Create your views here.
def purchase_officer(request):
    return redirect('PO-inventory')


def getRole(request):
    return Profile.objects.get(Owner=request.user).Role


@login_required(login_url='login')
def inventory(request):
    if getRole(request) == "PO":
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

        return render(request, 'PO-inventory.html', {'inventory': inventory})
    else:
        return redirect('login')


@login_required(login_url='login')
def pending_request(request):
    if getRole(request) == "PO":
        quotations = Quotation.objects.filter(Status='Pending').order_by().distinct('Bill')
        if request.method == 'POST':
            RegNo = request.POST.get('RegNo')
            return redirect(f'./show-quotation/{RegNo}')
        return render(request, 'PO-pending-request.html', {'quotations': quotations})
    else:
        return redirect('login')


@login_required(login_url='login')
def pending_request_show_quotation(request, RegNo):
    if getRole(request) == "PO":
        quotations = Quotation.objects.filter(Bill__RegNo=RegNo, Status='Pending')
        if request.method == 'POST':
            QuotationLink = request.POST.get('QuotationLink')
            if request.POST.get('Accept'):
                try:
                    with transaction.atomic():
                        for quotation in quotations:
                            if quotation.QuotationLink == QuotationLink:
                                quotation.Status = 'Approved'
                                Purchase.objects.create(Bill=Bill.objects.get(RegNo=RegNo), Quotation=quotation).save()
                            else:
                                quotation.Status = 'Declined'
                            quotation.save()
                    messages.success(request, 'Quotation approved')
                    return redirect('pending-request')
                except:
                    # print("error")
                    messages.error(request, "Some error Occurred !")
            elif request.POST.get('Reject'):
                quotation = quotations.get(QuotationLink=QuotationLink)
                quotation.Status = 'Declined'
                quotation.save()
            return redirect(f'/purchase-officer/pending-request/show-quotation/{RegNo}')
        return render(request, 'PO-pending-request-show-quotation.html', {'quotations': quotations})
    else:
        return redirect('login')


@login_required(login_url='login')
def request_history(request):
    if getRole(request) == "PO":
        quotations = Quotation.objects.filter(Status__in=['Approved', 'Declined']).order_by('-Bill')
        return render(request, 'PO-request-history.html', {'quotations': quotations})
    else:
        return redirect('login')
