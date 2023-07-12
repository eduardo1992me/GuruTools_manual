from bbk_soup import monitoreo_booking

url = "https://www.booking.com/hotel/mx/francia-aguascalientes.es.html?checkin=2023-12-28&checkout=2023-12-29&group_adults=2&group_children=0&no_rooms=1&selected_currency=MXN"
cycle = 0

monitoreo = monitoreo_booking(url, cycle)
resultado = monitoreo.monitoreo_bbk()
print("Esto es lo que devuelve ya en la clase gestor_monitoreo: ")
print(resultado)