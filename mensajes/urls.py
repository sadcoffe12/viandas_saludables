from django.urls import path
from . import views

urlpatterns = [
    path('', views.bandeja_entrada, name='bandeja'),
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('ver/<int:mensaje_id>/', views.ver_mensaje, name='ver_mensaje'),
    path('responder/<int:mensaje_id>/', views.responder_rapido, name='responder_rapido'),

]
