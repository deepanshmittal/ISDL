from django.contrib.auth.decorators import login_required
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
        return render(request, 'PO-inventory.html', {'inventory': inventory})
    else:
        return redirect('login')


@login_required(login_url='login')
def pending_request(request):
    if getRole(request) == "PO":
        quotations = Quotation.objects.filter(Status='Pending').order_by('Bill__Date').distinct()
        if request.method == 'POST':
            RegNo = request.POST.get('RegNo')
            return redirect(f'./show-quotation/{RegNo}')
        return render(request, 'PO-pending-request.html', {'quotations': quotations})
    else:
        return redirect('login')


@login_required(login_url='login')
def pending_request_show_quotation(request, RegNo):
    if getRole(request) == "PO":
        quotations = Quotation.objects.filter(Bill=Bill.objects.get(RegNo=RegNo), Status='Pending')
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
