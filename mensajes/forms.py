from django import forms
from .models import Mensaje
from django.contrib.auth.models import User

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['receptor', 'contenido']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        # Usuario común: solo puede enviar a staff
        if not user.is_staff and not user.is_superuser:
            self.fields['receptor'].queryset = User.objects.filter(is_staff=True)
        else:
            # Staff/Admin: puede enviar a todos
            self.fields['receptor'].queryset = User.objects.exclude(id=user.id)
