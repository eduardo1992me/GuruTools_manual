from rest_framework import serializers
from .models import Hotel



class HotelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hotel
        fields = ('pk','nombre', 'categoria', 'pais', 'estado', 'direccion', 'fecha_alta', 'activo', 'id_usuario_id' )
