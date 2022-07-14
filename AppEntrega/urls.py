from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio,name="" ),
    path('clientes/', clientes, name="clientes"),
    path('productos/', productos, name="productos") ,
    path('proveedores/', proveedores, name="proveedores"),
    path('clientesforms/',ClientesFormulario, name="clientesFormulario"),
    path('proveforms/',ProveedoresFormulario, name="proveedoresFormulario"),

]