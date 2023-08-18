from .bbk_soup import Monitoreo_booking
from .site_2023 import Monitoreo_sito_2023
from .exp_soup_v2 import Monitoreo_expedia
from .models import ControlMonitoreos, Monitoreos, Hotel, Habitaciones, HabitacionesHijas
from datetime import date, datetime
import locale
locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')




class Monitoreo_Clase:

    def monitoreo_general():
        url_bbk = "https://www.booking.com/hotel/mx/francia-aguascalientes.es.html?checkin=2023-12-28&checkout=2023-12-29&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
        url_s_2023 = "https://cabinasyafethosa.com"
        url_exp = "https://www.expedia.mx/Aguascalientes-Hoteles-Fiesta-Americana-Aguascalientes.h2517.Informacion-Hotel?chkin=2023-07-19&chkout=2023-07-20&x_pwa=1&rfrr=HSR&pwa_ts=1689234481442&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5teC9Ib3RlbC1TZWFyY2g%3D&useRewards=true&rm1=a2&regionId=315&destination=Aguascalientes%2C+Aguascalientes%2C+México&destType=MARKET&latLong=21.880852%2C-102.296016&showAvailableOnly=true&sort=RECOMMENDED&top_dp=1526&top_cur=MXN&userIntent=&selectedRoomType=200074233&selectedRatePlan=200445122&searchId=2951c8ae-8429-4c15-b523-515419313d3c"

        cycle = 0
        hotel_id = Hotel.objects.get(pk=2)
        control_monitoreo = ControlMonitoreos(fecha_ejecucion = date.today(), id_hotel = hotel_id, fecha_monitoreo = date.today(), hora_monitoreo = str(datetime.now())[11:16])
        control_monitoreo.save()
        id_monitoreo = control_monitoreo.pk
        instancia_control_m = ControlMonitoreos.objects.get(pk=id_monitoreo)


        # Booking
        monitoreo_bbk = Monitoreo_booking(url_bbk, cycle)
        rango_ciclo = 0
        resultado_bbk = monitoreo_bbk.monitoreo_bbk()
        

        for fecha in resultado_bbk:

            for hab in resultado_bbk[fecha]:
                print(fecha)
                print(hab)
                print(resultado_bbk[fecha][hab])
                insercion_monitoreo = Monitoreos(id_monitoreo_p = instancia_control_m, fecha_chkin = fecha, canal = "booking", moneda = url_bbk[-3:], rango = str(rango_ciclo), tarifa = locale.atof(resultado_bbk[fecha][hab]), habitacion = hab)
                
                insercion_monitoreo.save()
                print("Se completo Booking")
            rango_ciclo += 1
        

        # Sitio Guruhotel 2023
        monitoreo_sitio_2023 = Monitoreo_sito_2023(url_s_2023, cycle)
        rango_ciclo = 0
        resultado_s_2023 = monitoreo_sitio_2023.monitoreoSitio_2023()
        for fecha in resultado_s_2023:
            for hab in resultado_s_2023[fecha]:
                insercion_monitoreo = Monitoreos(id_monitoreo_p = instancia_control_m, fecha_chkin = fecha, canal = "web", moneda = "MXN", rango = str(rango_ciclo), tarifa = locale.atof(resultado_s_2023[fecha][hab]), habitacion = hab)
                
                insercion_monitoreo.save()
                print("Se completo Sitio Guru 2023")
            rango_ciclo += 1


        # Expedia
        monitoreo_exp = Monitoreo_expedia(url_exp, cycle)
        rango_ciclo = 0
        resultado_expedia = monitoreo_exp.monotoreoExpedia()
        for fecha in resultado_expedia:
            for hab in resultado_expedia[fecha]:
                if resultado_expedia[fecha][hab] is not None:
                    insercion_monitoreo = Monitoreos(id_monitoreo_p = instancia_control_m, fecha_chkin = fecha, canal = "expedia", moneda = "MXN", rango = str(rango_ciclo), tarifa = locale.atof(resultado_expedia[fecha][hab]), habitacion = hab)
                
                    insercion_monitoreo.save()
                print("Se completo Expedia")
            rango_ciclo += 1
    


    def monitoreo_habitaciones():
        url_bbk = "https://www.booking.com/hotel/mx/francia-aguascalientes.es.html?checkin=2023-12-28&checkout=2023-12-29&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
        url_s_2023 = "https://cabinasyafethosa.com"
        url_exp = "https://www.expedia.mx/Aguascalientes-Hoteles-Fiesta-Americana-Aguascalientes.h2517.Informacion-Hotel?chkin=2023-07-19&chkout=2023-07-20&x_pwa=1&rfrr=HSR&pwa_ts=1689234481442&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5teC9Ib3RlbC1TZWFyY2g%3D&useRewards=true&rm1=a2&regionId=315&destination=Aguascalientes%2C+Aguascalientes%2C+México&destType=MARKET&latLong=21.880852%2C-102.296016&showAvailableOnly=true&sort=RECOMMENDED&top_dp=1526&top_cur=MXN&userIntent=&selectedRoomType=200074233&selectedRatePlan=200445122&searchId=2951c8ae-8429-4c15-b523-515419313d3c"

        cycle = 0
        hotel_id = Hotel.objects.get(pk=2)
        control_monitoreo = ControlMonitoreos(fecha_ejecucion = date.today(), id_hotel = hotel_id, fecha_monitoreo = date.today(), hora_monitoreo = str(datetime.now())[11:16])
        control_monitoreo.save()
        id_monitoreo = control_monitoreo.pk
        instancia_control_m = ControlMonitoreos.objects.get(pk=id_monitoreo)


        # Booking
        monitoreo_bbk = Monitoreo_booking(url_bbk, cycle)
        rango_ciclo = 0
        resultado_bbk = monitoreo_bbk.monitoreo_bbk_hab()


        insercion_monitoreo = Habitaciones(id_monitoreo_p = instancia_control_m, fecha_chkin = fecha, canal = "booking", moneda = url_bbk[-3:], rango = str(rango_ciclo), tarifa = locale.atof(resultado_bbk[fecha][hab]), habitacion = hab)
        
        insercion_monitoreo.save()
        print("Se completo Booking")
            
        

        # Sitio Guruhotel 2023
        monitoreo_sitio_2023 = Monitoreo_sito_2023(url_s_2023, cycle)
        rango_ciclo = 0
        resultado_s_2023 = monitoreo_sitio_2023.monitoreoSitio_2023()
        for fecha in resultado_s_2023:
            for hab in resultado_s_2023[fecha]:
                insercion_monitoreo = Monitoreos(id_monitoreo_p = instancia_control_m, fecha_chkin = fecha, canal = "web", moneda = "MXN", rango = str(rango_ciclo), tarifa = locale.atof(resultado_s_2023[fecha][hab]), habitacion = hab)
                
                insercion_monitoreo.save()
                print("Se completo Sitio Guru 2023")
            rango_ciclo += 1


        # Expedia
        monitoreo_exp = Monitoreo_expedia(url_exp, cycle)
        rango_ciclo = 0
        resultado_expedia = monitoreo_exp.monotoreoExpedia()
        for fecha in resultado_expedia:
            for hab in resultado_expedia[fecha]:
                if resultado_expedia[fecha][hab] is not None:
                    insercion_monitoreo = Monitoreos(id_monitoreo_p = instancia_control_m, fecha_chkin = fecha, canal = "expedia", moneda = "MXN", rango = str(rango_ciclo), tarifa = locale.atof(resultado_expedia[fecha][hab]), habitacion = hab)
                
                    insercion_monitoreo.save()
                print("Se completo Expedia")
            rango_ciclo += 1
