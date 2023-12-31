from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import HotelForm, ConexionForm, HabitacionesForm # <-- Paso 2 para formulario con la información del modelo usando el modulo forms.py(creado por nosotros) importarlo
from .models import Hotel, Conexion, Habitaciones # <-- Luego importado para interactuar con la base de datos para poder listar los hoteles
from rest_framework import viewsets, status
from .serializers import HotelSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .gestor_monitoreo import *
from .Test_Registro import *
from .hotelRegister import *

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


"""class hotelView(viewsets.ModelsViewSet):
    serealizer_class = HotelSerializer
    queryset = Hotel.objects.all()"""

@api_view(['GET', 'POST'])
def hotel_list_a(request):
    if request.method == 'GET':
        data = Hotel.objects.all()

        serializers = HotelSerializer(data, context={'request': request}, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = HotelSerializer(data=request.data)
        print(f"Lo que tiene Serealizer es {serializers}")
        if serializers.is_valid():
            serializers.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def hotel_detail_a(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializers = HotelSerializer(Hotel, data=request.data, context={'request':request})
        if serializers.is_valid():
            serializers.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def hotel_full_a(request):
    
    if request.method == 'POST':
        peticion_monitoreo = Monitoreo_Clase.monitoreo_general()
        

        return Response(status=status.HTTP_202_ACCEPTED)
    

@api_view(['GET', 'POST'])
def registro_test(request):
    if request.method == 'POST':
        data=request.data
        clean_data = []
        for i in data:
            clean_data.append(data[i])
        print(clean_data)

        nombre = clean_data[1]
        categoria = clean_data[2]
        edad = clean_data[3]
        peticion_registro = Registro_Test1.guardarEnDB(nombre, categoria, edad)

        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def registro_gen_1(request):
    if request.method == 'POST':
        data=request.data
        clean_data = []
        for i in data:
            clean_data.append(data[i])
        print(clean_data)

        name = clean_data[1]
        category = clean_data[2]
        country = clean_data[3]
        state = clean_data[4]
        address = clean_data[5]
        url = clean_data[6]
        url_exp = clean_data[7]
        url_bbk = clean_data[8]

        peticion_registro = HotelRegister.save_general_register_1(name, category, country, state, address, url, url_exp ,url_bbk)
        new_hotel_id = str(peticion_registro)
        resonse_data = {'id': new_hotel_id}
        print(f"En view devuelve: {resonse_data}")
        return Response(resonse_data, status=status.HTTP_201_CREATED)