from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import *

ROLE = {'IM': 'inventory-manager',
        'PO': 'purchase-officer',
        'MGIM': 'main-gate-inventory-manager',
        }


# Create your views here.
def home(request):
    return redirect('login')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect(f'/{ROLE[getRole(request)]}')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist !!')
            return redirect('home')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f'/{ROLE[getRole(request)]}')
        else:
            messages.error(request, 'Invalid Credentials !')
            return redirect('home')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')


def getRole(request):
    return Profile.objects.get(Owner=request.user).Role
