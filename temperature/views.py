from django.shortcuts import render, HttpResponse
import requests

def temperature(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET and 'latitud' in request.GET and 'longitud' in request.GET and 'tipo_terreno' in request.GET:
        value = request.GET['value']
        latitud = request.GET['latitud']
        longitud = request.GET['longitud']
        tipo_terreno = request.GET['tipo_terreno']
        # Verifica si el value no esta vacio
        if value and latitud and longitud and tipo_terreno:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': '°C', 'value': value, 'latitud':latitud, 'longitud': longitud, 'tipo_terreno': tipo_terreno}
            #response = requests.post('http://127.0.0.1:8000/temperature/', args)
            response = requests.post('http://pi1-eafit-samorenoq.azurewebsites.net/temperature/', args)
            # Convierte la respuesta en JSON
            temperature_json = response.json()

    # Realiza una petición GET al Web Services
    #response = requests.get('http://127.0.0.1:8000/temperature/')
    response = requests.get('http://pi1-eafit-samorenoq.azurewebsites.net/temperature/')
    # Convierte la respuesta en JSON
    temperatures = response.json()
    return render(request, "temperature/temperature.html", {"temperatures" : temperatures})