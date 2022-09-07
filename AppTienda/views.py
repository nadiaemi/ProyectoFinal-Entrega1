from django.shortcuts import render
from django.http import HttpResponse
from .models import Comidas, Bebidas, Otros
from AppTienda.forms import ComidasForm, BebidasForm, OtrosForm

# Create your views here.

def inicio (request):
    return render (request, 'inicio.html')

# VISTAS PARA LA CARGA DE COMIDAS EN EL FORMULARIO, BUSQUEDA Y MUESTRA DE RESULTADOS

def comidas(request):
    if request.method == 'POST':
        form = ComidasForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion['nombre']
            marca = informacion['marca']
            precio = informacion['precio']
            comida = Comidas(nombre = nombre, marca = marca, precio = precio)
            comida.save()
            return render (request, 'inicio.html')
    else:
        formulario = ComidasForm()
        return render (request, 'comidas.html', {'formulario': formulario})


def busquedaComidas(request):
    return render (request, 'busquedaComidas.html')

def buscarComidas(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        comida= Comidas.objects.filter(nombre__icontains = nombre)
        return render (request, 'resultadoComidas.html', {'comidas': comida})
    
    else:
        return render (request, 'busquedaComidas.html', {'mensaje': 'Ingrese un dato!'})

    return HttpResponse(respuesta)   

#.............................................................................

# VISTAS PARA LA CARGA DE BEBIDAS EN EL FORMULARIO, BUSQUEDA Y MUESTRA DE RESULTADOS

def bebidas (request):
    if request.method == 'POST':
        form = BebidasForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion['nombre']
            marca = informacion['marca']
            precio = informacion['precio']
            bebida = Bebidas(nombre = nombre, marca = marca, precio = precio)
            bebida.save()
            return render (request, 'inicio.html')
    else:
        formulario = BebidasForm()
        return render (request, 'bebidas.html', {'formulario': formulario})

def busquedaBebidas(request):
    return render (request, 'busquedaBebidas.html')

def buscarBebidas(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        bebida= Bebidas.objects.filter(nombre__icontains = nombre)
        return render (request, 'resultadoBebidas.html', {'bebidas': bebida})
    
    else:
        return render (request, 'busquedaBebidas.html', {'mensaje': 'Ingrese un dato!'})

    return HttpResponse(respuesta)   

#............................................................................

# VISTAS PARA LA CARGA DE BEBIDAS EN EL FORMULARIO, BUSQUEDA Y MUESTRA DE RESULTADOS

def otros (request):
    if request.method == 'POST':
        form = OtrosForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion['nombre']
            marca = informacion['marca']
            precio = informacion['precio']
            otro = Otros(nombre = nombre, marca = marca, precio = precio)
            otro.save()
            return render (request, 'inicio.html')
    else:
        formulario = OtrosForm()
        return render (request, 'otros.html', {'formulario': formulario})

def busquedaOtros(request):
    return render (request, 'busquedaOtros.html')

def buscarOtros(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        otro= Otros.objects.filter(nombre__icontains = nombre)
        return render (request, 'resultadoOtros.html', {'otros': otro})
    
    else:
        return render (request, 'busquedaOtros.html', {'mensaje': 'Ingrese un dato!'})

    return HttpResponse(respuesta)  