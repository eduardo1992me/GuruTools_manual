from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import HotelForm, ConexionForm, HabitacionesForm # <-- Paso 2 para formulario con la información del modelo usando el modulo forms.py(creado por nosotros) importarlo
from .models import Hotel, Conexion, Habitaciones # <-- Luego importado para interactuar con la base de datos para poder listar los hoteles


# Create your views here.
def home(request):
    return render(request, 'home.html')


def hotel(request):
    hotel_list = Hotel.objects.all() # <--- Devuelve todos los hoteles en forma de lista y se guarda en una variable
    hotel_conexion = Conexion.objects.all()
    hotel_habitaciones = Habitaciones.objects.all()
    return render(request, 'hotel.html', {'hotel_list' : hotel_list, 'hotel_conexion': hotel_conexion,'hotel_habitaciones': hotel_habitaciones }) # <-- Luego de esto vamos a hotel.html para mostrarlos

def create_hotel(request):
    if request.method == 'GET':
        return render(request, 'create_hotel.html', { # <-- Una vez que se creo el archivo html se viene a Views.py y se crea la función con el nombre y se le indica que se retorna con render dicho archivo para luego dar de alta la url nueva en url.py
        'form': HotelForm 
    
        }) # Paso 3 formulario desde modelo: Ya importado se usa en esta funión para luego mandarlo llamar directo en el html de la vista(create_hotel.html)
    else:
        try:
            form = HotelForm(request.POST)
            new_hotel = form.save() # <--- Esta linea y la anterior sirven para que la información del formulario se use para ser guardada con el metodo save()
            return redirect('hotel')
        except ValueError:
            return render(request, 'create_hotel.html', { 
                'form': HotelForm,
                'error': 'Por favor provee datos validos'
            })

        #return render(request, 'create_hotel.html', { # <-- Una vez que se creo el archivo html se viene a Views.py y se crea la función con el nombre y se le indica que se retorna con render dicho #archivo para luego dar de alta la url nueva en url.py
        #'form': HotelForm
        #})


def hotel_detail(request, hotel_id): 
    if request.method == 'GET':
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        form = HotelForm(instance=hotel)
        return render(request, 'hotel_detail.html', {'hotel': hotel, 'form': form})
    else:
        try:
            hotel = get_object_or_404(Hotel, pk=hotel_id)
            form = HotelForm(request.POST, instance=hotel)
            form.save()
            return redirect('hotel')
        except:
            return render(request, 'hotel_detail.html', {'hotel': hotel, 'form': form, 'error': "Error Actualizando información del hotel"})
        

def conexion(request, hotel_id):
    if request.method == 'GET':
        return render(request, 'conexion.html', {'hotel': hotel, 'form': ConexionForm, 'form2': HabitacionesForm})
    else:
        form = ConexionForm(request.POST)
        form2 = HabitacionesForm(request.POST)
        nueva_conexion = form.save(commit=False)
        nueva_conexion2 = form2.save(commit=False)
        nueva_conexion.save()
        nueva_conexion2.save()
        return redirect('hotel')
        
        # hotel = Hotel.objects.get(pk=hotel_id)
    