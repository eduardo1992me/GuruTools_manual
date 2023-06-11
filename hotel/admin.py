from django.contrib import admin
from .models import Hotel, Conexion, Habitaciones, Canales

class HotelAdmin(admin.ModelAdmin):
 readonly_fields = () # <--- Aquí se crea la clase HotelAdmin donde se indican los datos que son de solo lectura en el Administrador de Django  "fecha_alta", 

# Register your models here.
admin.site.register(Hotel, HotelAdmin)  # <--- Y aquí se muestra ese campo en el detalle del hotel en el administrador de Django
admin.site.register(Conexion, HotelAdmin)
admin.site.register(Canales, HotelAdmin)

admin.site.register(Habitaciones, HotelAdmin)