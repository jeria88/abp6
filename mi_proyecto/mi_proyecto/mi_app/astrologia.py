# mi_app/astrologia.py

def obtener_signo_solar(dia, mes):
    signos = [
        (20, "Capricornio"), (19, "Acuario"), (20, "Piscis"), (20, "Aries"),
        (21, "Tauro"), (21, "Géminis"), (22, "Cáncer"), (22, "Leo"),
        (23, "Virgo"), (23, "Libra"), (23, "Escorpio"), (21, "Sagitario"),
        (31, "Capricornio")
    ]
    if dia > signos[mes-1][0]:
        return signos[mes][1]
    else:
        return signos[mes-1][1]

def calcular_carta(nombre, fecha_nac, hora_nac):
    # Lógica simplificada para fines educativos
    dia = fecha_nac.day
    mes = fecha_nac.month
    
    sol = obtener_signo_solar(dia, mes)
    # Simulamos Luna y Ascendente basados en la hora y dia para que varíe
    signos_lista = ["Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", 
                    "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"]
    
    luna = signos_lista[(dia + mes) % 12]
    ascendente = signos_lista[(hora_nac.hour + mes) % 12]
    
    return {
        "nombre": nombre,
        "sol": sol,
        "luna": luna,
        "ascendente": ascendente
    }