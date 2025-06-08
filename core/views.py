from django.shortcuts import render, redirect
from .forms import ProductoForm, ClienteForm, PedidoForm
from .models import Producto, Cliente, Pedido
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from mensajes.models import Mensaje
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class ListarModeloMixin(LoginRequiredMixin, ListView):
    template_name = ""
    context_object_name = "resultados"
    campo_busqueda = "" 

    def get_queryset(self):
        query = self.request.GET.get(self.query_param)
        if query:
            filtro = {f"{self.campo_busqueda}__icontains": query}
            return self.model.objects.filter(**filtro)
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get(self.query_param, "")
        return context

class ListarProductoView(ListarModeloMixin):
    model = Producto
    template_name = "core/buscar.html"
    campo_busqueda = "nombre"
    query_param = "nombre"

class ListarPedidoView(ListarModeloMixin):
    model = Pedido
    template_name = "core/buscar_pedidos.html"
    campo_busqueda = "cliente__nombre"
    query_param = "cliente"

    def get_queryset(self):
        user = self.request.user
        query = self.request.GET.get(self.query_param)

        if user.is_staff or user.is_superuser:
            if query:
                return Pedido.objects.filter(cliente__nombre__icontains=query)
            return Pedido.objects.all()
        
        try:
            cliente = Cliente.objects.get(user=user)
        except Cliente.DoesNotExist:
            return Pedido.objects.none()

        pedidos = Pedido.objects.filter(cliente=cliente)
        if query:
            pedidos = pedidos.filter(cliente__nombre__icontains=query)
        return pedidos

def home(request):
    sin_leer = 0
    if request.user.is_authenticated:
        sin_leer = Mensaje.objects.filter(receptor=request.user, leido=False).count()
    return render(request, 'core/home.html', {'sin_leer': sin_leer})

def about(request):
    return render(request, 'core/about.html')

def es_staff(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(es_staff)
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    return render(request, 'core/producto_form.html', {'form': form})

@user_passes_test(es_staff)
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'core/cliente_form.html', {'form': form})

@login_required
def agregar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.cliente = request.user.cliente
            pedido.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = PedidoForm()
    return render(request, 'core/pedido_form.html', {'form': form})


@login_required
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

@login_required
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




