from django.shortcuts import render, redirect
from .forms import ProductoForm, ClienteForm, PedidoForm
from .models import Producto, Cliente, Pedido

def home(request):
    return render(request, 'core/home.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    return render(request, 'core/producto_form.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'core/cliente_form.html', {'form': form})

def agregar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PedidoForm()
    return render(request, 'core/pedido_form.html', {'form': form})

def buscar_producto(request):
    resultados = []
    query = ""

    if request.method == "GET" and "nombre" in request.GET:
        query = request.GET["nombre"]
        resultados = Producto.objects.filter(nombre__icontains=query)

    return render(request, "core/buscar.html", {
        "resultados": resultados,
        "query": query
    })

def buscar_pedido(request):
    pedidos = []
    query = ""

    if request.method == "GET" and "cliente" in request.GET:
        query = request.GET["cliente"]
        pedidos = Pedido.objects.filter(cliente__nombre__icontains=query)

    return render(request, "core/buscar_pedidos.html", {
        "pedidos": pedidos,
        "query": query
    })

