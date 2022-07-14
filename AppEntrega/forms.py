from django import forms

class ClientesForms(forms.Form):
    nombre= forms.CharField()
    direccion= forms.CharField()
    dni= forms.IntegerField()

class ProveedoresForms(forms.Form):
    nombre= forms.CharField()
    direccion= forms.CharField()
    cantidad_de_productos= forms.IntegerField()

class ProductosForms(forms.Form):
    marca= forms.CharField()
    precio= forms.IntegerField()
    cantidad= forms.IntegerField()