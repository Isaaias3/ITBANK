"""ITBANK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from mailbox import NoSuchMailboxError
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from register import views as views_register
from homebanking import views as views_homebanking
from api import views as API_views

urlpatterns = [
    path('', RedirectView.as_view(url='accounts/login/', permanent=True), name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registro.html', views_register.register, name="registro"),
    path('home/', views_homebanking.home, name="inicio"),
    path('home/cotizaciones', views_homebanking.cotizaciones, name="cotizaciones"),
    path('home/edit_profile', views_homebanking.EditProfile, name="EditProfile"),
    path('api/sucursales/', API_views.SucursalesList.as_view(),name='api_sucursales'),
    path('api/cliente/', API_views.ClienteList.as_view(),name='api_cliente'),
    path('api/cuenta/', API_views.CuentaList.as_view(),name='api_cuenta'),
    path('admin/', admin.site.urls),
]

from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)