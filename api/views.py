from curses.ascii import ESC
from multiprocessing.connection import Client
from urllib import response
from django.shortcuts import render
from rest_framework import permissions
from .permissions import EsCliente
from .serializers import ClienteSerializer, CuentaSerializer, SucursalSerializer

# Create your views here.
from clientes.models import Sucursal, Cliente
from cuentas.models import Cuenta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SucursalesList(APIView):
    def get(self, request):
        sucursales = Sucursal.objects.all()
        serializer = SucursalSerializer(sucursales, many = True)

        if sucursales:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_404_NOT_FOUND)


class ClienteList(APIView):
    permission_classes = [permissions.IsAuthenticated, EsCliente]

    def get(self, request):

        cliente= Cliente.objects.filter(customer_dni = request.user).all()
        serializer = ClienteSerializer(cliente, many= True) 

        if cliente:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_404_NOT_FOUND)

class CuentaList(APIView):
    permission_classes = [permissions.IsAuthenticated, EsCliente]

    def get(self, request):
        cliente = Cliente.objects.filter(customer_dni = request.user).first()
        cuenta = Cuenta.objects.filter(customer= cliente)
        serializer = CuentaSerializer(cuenta, many= True)

        if cuenta:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_404_NOT_FOUND)

        