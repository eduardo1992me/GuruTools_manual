from .models import Hotel
from datetime import timedelta, date

class HotelRegister:
    def save_general_register_1(name, category, country, state, address, url, url_exp ,url_bbk):
        insert_date = date.today()

        insert_data = Hotel(nombre = name, categoria = category, activo = True, pais = country, estado = state, direccion = address, fecha_alta = insert_date, url_canal = url, url_canal_exp = url_exp, url_canal_bbk = url_bbk)
        insert_data.save()
        print(f"Hotel Guardado correctamente, con id:{insert_data.pk}")
        return insert_data.pk