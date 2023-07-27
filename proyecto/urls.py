"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from veterinaria.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home),
    path('home/',inicio, name='Home'),
    path('ingresarMascota/',IngresarMascota, name = 'mascota'),
    path('ingresarfactura/',IngresarFactura, name = 'factura'),
    path('menuVendedor/',menuVendedor, name= "menuVendedor"),
    path('menuVeterinario/',menuVeterinario, name = "menuVeterinario"),
    path('registro/', registarDuenoMascota, name='registro' ),
    path('historia/', post, name = 'historia'),
    path('Verhistoria/', MostarHistoriaclinica, name = 'Verhistoria'),
    path('VerOrden/', mostrarListado, name = 'orden'),
    path('VerOrdenVendedor/', mostrarListadoOrdenVendedor, name = 'ordenVendedor'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('actualizarOrden/<int:id>', actualizarOrden),
    path('VerMascota/', verMascota, name = 'verMascota'),
    path('paginaerror/', rutaIncorrecta, name = 'rutaIncorrecta')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Ruta para capturar errores 404
urlpatterns += [
    path('<path:not_found>/', custom_page_not_found),
]

# Configuración de la vista personalizada para el error 404
handler404 = custom_page_not_found
