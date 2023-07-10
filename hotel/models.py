from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hotel(models.Model):
#    id_hotel  <--- Al parecer al mandarlo crear así en automatico agregara un ID... esta por verse...
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # <---- Esto hace refefrencia a la tabla User que viene de default con la creación de Django y en caso de que el usuario sea borrado se borraran sus hoteles relacionados
    nombre = models.CharField(max_length=40)
    categoria = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)
    pais = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    direccion = models.TextField(blank=True)
    fecha_alta = models.DateTimeField(auto_now_add=True) # Esta prpoiedad del final es para que se rellene en automatico la fecha y hora


    def __str__(self):  # <--- Esto srive para que en el administrador nativo de django en la lista de hoteles muestre el nombre y si esta activo o no
        if self.activo == True:
            estatus = "Activo"
        else:
            estatus = "Inactivo"
        return self.nombre + ' -  Estado: ' + estatus

class Canales(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    
class Conexion(models.Model):
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_canal = models.ForeignKey(Canales, on_delete=models.CASCADE)
    url_canal = models.TextField(blank=False)
    fecha_alta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_hotel) + ' -Canal: ' + str(self.id_canal)

class Habitaciones(models.Model):
    id_conexion = models.ForeignKey(Conexion, on_delete=models.CASCADE)
    id_canal = models.ForeignKey(Canales, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    
class ControlMonitoreos(models.Model):
    fecha_ejecucion = models.DateTimeField(auto_now_add=True)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    # id_usuario = 
    fecha_monitoreo = models.DateField(auto_now_add=True)
    hora_monitoreo = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.fecha_ejecucion

class Monitoreos(models.Model):
    id_monitoreo_p = models.ForeignKey(ControlMonitoreos, on_delete=models.CASCADE)
    fecha_chkin = models.DateField()
    canal = models.CharField(max_length=30)
    moneda = models.CharField(max_length=5)
    rango = models.CharField(max_length=5)
    tarifa = models.FloatField()
    habitacion = models.TextField()

    def __str__(self):
        return self.fecha_chkin

