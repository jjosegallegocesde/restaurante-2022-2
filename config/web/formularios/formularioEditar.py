#LOS FORMULARIOS DE DJANGO SON CLASES

from django import forms


class FormularioEditar(forms.Form):


    precioPlato=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=5
    )