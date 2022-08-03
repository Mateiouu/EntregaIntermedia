from django import forms

class AtletaFormulario(forms.Form):

    nombre = forms.CharField(max_length = 40)
    apellido = forms.CharField(max_length = 40)
    nacimiento = forms.DateField()
    diciplina = forms.CharField(max_length = 40)
    pais = forms.CharField(max_length = 40)

class EntrenadorFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length= 30)
    entrena = forms.CharField(max_length=30)
    email = forms.EmailField()


class DeporteFormulario(forms.Form):

   nombre = forms.CharField(max_length=30)
   incluye = forms.CharField(max_length=30)