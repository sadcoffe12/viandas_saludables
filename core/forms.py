from django import forms
from .models import Producto, Cliente, Pedido
from ckeditor.widgets import CKEditorWidget

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'descripcion': CKEditorWidget(),
        }
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['productos', 'estado']

class BuscarProductoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del producto")
