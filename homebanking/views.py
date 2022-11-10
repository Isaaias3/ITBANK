from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from clientes.models import Cliente
from cuentas.models import Cuenta
from django.urls import reverse

# Useful Functions
def Nombre(user):
    if len(user.customer_surname) > 5:
        nombre= user.customer_surname[0:5] + ", " + user.customer_name[0]
    else:
        nombre= user.customer_surname + ", " + user.customer_name[0]

    return nombre

def Image(user):
    aux = str(user.img_profile)

    return aux[(aux.rfind('media') + 6) ::]


# Create your views here.

@login_required
def home(request):
    cliente= Cliente.objects.get(customer_dni= request.user.username)
    cuenta= Cuenta.objects.get (customer_id= cliente.customer_id)

    nombre = Nombre(cliente)

    imagen= Image(cliente)
    
    return render(request, 'homebanking/home.html', {'name': nombre, 'surname': cliente.customer_surname, 'balance': cuenta.balance, 'numerocuenta': cuenta.account_id, 'img': imagen, 'username': cliente.customer_dni})

@login_required
def cotizaciones(request):
    return render(request, 'homebanking/cotizaciones.html')


# Edit Profile view with form
from random import randrange
from clientes.models import Cliente
from .forms import EditForm
from django.contrib.auth.models import User


@login_required
def EditProfile(request):
    cliente= Cliente.objects.get (customer_dni= request.user.username)

    nombre = Nombre(cliente)
    imagen = Image(cliente)

    return render(request, 'homebanking/edit_profile.html', {'name': nombre, 'img': imagen, 'username': cliente.customer_dni})
