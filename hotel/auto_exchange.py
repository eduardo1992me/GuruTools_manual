import requests
import json
import schedule
from .models import TipoDeCambio
from datetime import date, datetime


def get_exchange_rate():

    url = "https://v6.exchangerate-api.com/v6/9bc6401d9657ed634b9fbda5/latest/USD"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    datos_JSON = response.text
    #print(datos_JSON)
    datos_dicc = json.loads(datos_JSON)
    general_rate = (datos_dicc["conversion_rates"])
    print(general_rate["MXN"])
    rate = general_rate["MXN"]
    insertion_exchange_rate = TipoDeCambio (fecha_hora_t_cambio = str(datetime.now()), tipo_cambio = rate)
    insertion_exchange_rate.save()
    


schedule.every().day.at("06:00").do(get_exchange_rate)
schedule.every().day.at("12:00").do(get_exchange_rate)
schedule.every().day.at("15:00").do(get_exchange_rate)

# Bucle para ejecutar las tareas programadas
while True:
    schedule.run_pending()