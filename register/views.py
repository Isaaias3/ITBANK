from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from random import randrange

# Modelos utilizados.
from clientes.models import Cliente
from cuentas.models import Cuenta

# Create your views here.
from .forms import RegisterForm
from django.contrib.auth.models import User
from datetime import date

def register(request):
    registro_form = RegisterForm(request.POST, request.FILES)

    if request.method == "POST":
        if registro_form.is_valid():

            cliente_id = request.POST.get('cliente_id', "")
            pwd= request.POST.get('pwd', "")
            nombre= request.POST.get('nombre', "")
            apellido= request.POST.get('apellido', "")
            dob = request.POST.get('dob', "")
            tipo_cliente = request.POST.get('tipo_cliente', "")
            email= request.POST.get('email', "")
            img= registro_form.cleaned_data.get ('img_profile')


            user = User.objects.create_user (
                cliente_id,
                email,
                pwd,
                last_name= apellido, first_name= nombre, is_staff= False)
            user.save()

            cliente= Cliente.objects.create (
                customer_name = nombre, customer_surname= apellido,
                customer_dni= cliente_id, customer_type= tipo_cliente,
                branch_id= randrange(100), dob= dob, img_profile= img)
            cliente.save()

            cuenta= Cuenta.objects.create (
                customer= cliente, balance= 0, iban= 0 
            )
            cuenta.save()

        return redirect(reverse('login'))
    return render(request, "register/registro.html", {'form': registro_form})

def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html")