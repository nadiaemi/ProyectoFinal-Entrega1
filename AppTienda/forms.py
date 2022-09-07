from django import forms

class ComidasForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=40)
    precio = forms.IntegerField()

class BebidasForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=40)
    precio = forms.IntegerField()

class OtrosForm (forms.Form):
    nombre = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=40)
    precio = forms.IntegerField()