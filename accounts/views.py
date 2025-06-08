from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistroUsuarioForm, PerfilForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("home")
    else:
        form = RegistroUsuarioForm()
    return render(request, "accounts/registro.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def perfil(request):
    perfil = request.user.perfil
    return render(request, "accounts/perfil.html", {"perfil": perfil})

@login_required
def editar_perfil(request):
    perfil = request.user.perfil
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect("perfil")
    else:
        form = PerfilForm(instance=perfil)
    return render(request, "accounts/editar_perfil.html", {"form": form})
