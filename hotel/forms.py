from django.forms import ModelForm
from .models import Hotel, Conexion, Habitaciones
from django.utils.translation import gettext_lazy as _

"""Aquí lo que estoy haciendo es en lugar de crear un form para el formulario con HTML manualmente uso esta clase para crear un formulario que se base en models(los campos de la BD) para crearlo automaticamente"""

class HotelForm(ModelForm): # <-- Paso 1: crear esta clase con los campos que se van a requerir para luego ir a view a implementarlo en la vista(views.py)
    class Meta:
        model = Hotel
        fields = ['nombre', 'categoria', 'activo', 'pais', 'estado', 'direccion']
        labels = {
            "nombre": _("Nombre del Hotel"), "activo": _("Estatus del hotel(Activo/Inactivo)")}
        model2 = Conexion
        fields2 = ['url_canal']
        model3 = Habitaciones
        fields3 = ['nombre']



class ConexionForm(ModelForm):
    class Meta:
        model = Conexion
        fields = ['url_canal']

class HabitacionesForm(ModelForm):
    class Meta:
        model = Habitaciones
        fields = ['nombre']