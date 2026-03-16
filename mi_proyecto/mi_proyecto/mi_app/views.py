# mi_app/views.py

def inicio(request):
    return render(request, 'inicio.html')

from django.shortcuts import render
from datetime import datetime
from .astrologia import calcular_carta

def inicio(request):
    resultado = None
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        fecha_str = request.POST.get("fecha")
        hora_str = request.POST.get("hora")
        
        if fecha_str and hora_str:
            fecha_nac = datetime.strptime(fecha_str, '%Y-%m-%d')
            hora_nac = datetime.strptime(hora_str, '%H:%M')
            resultado = calcular_carta(nombre, fecha_nac, hora_nac)

    return render(request, 'inicio.html', {'resultado': resultado})

