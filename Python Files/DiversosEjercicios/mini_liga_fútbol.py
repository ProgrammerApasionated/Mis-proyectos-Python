# def obtener_resultados()                  ->   Mediante el input del usuario va calculando unos parámetros.

# def racha_de_partidos(lista_resultados)   ->   Mediante una lista saca la racha de victorias.


def obtener_resultados():
    lista_resultados = []
    cadena = input ("Introduce el resultado del partido :  (V = Victoria, D = Derrota o E = Empate : \n")
    resultado = 0
    partidos = 0
    while cadena in ("V", "D", "E"):
        if cadena == "V":
            resultado += 3
            lista_resultados.append("V")
        elif cadena == "E" :
            resultado += 1
            lista_resultados.append("E")
        else :
            lista_resultados.append("D")
        partidos += 1
        cadena = input ("Introduce el resultado del partido :  (V = Victoria, D = Derrota o E = Empate : \n")
    return lista_resultados, resultado, partidos

def racha_partidos (lista_de_resultados):
    inicio = -1
    longitud = 0
    mayor_inicio = -1
    mayor_longitud = -1
    mayor_final = -1
    i= 0
    while i < len(lista_de_resultados):
        if lista_de_resultados[i] == "V":
            if longitud == 0 :
                inicio = i
            longitud += 1
        else :
            if longitud > mayor_longitud:
                mayor_inicio = inicio
                mayor_longitud = longitud
                mayor_final = i - 1
            longitud = 0
        i += 1
        if longitud > mayor_longitud:
            mayor_inicio = inicio
            mayor_longitud = longitud
            mayor_final = i - 1
    if mayor_longitud > 0 :
        print(f"La racha de partidos con más victoria ha empezado en el partido {mayor_inicio + 1} y ha acabado en el partido {mayor_final + 1} ")
        print(f"Ha tenido una racha de {mayor_longitud} victorias. Felicidades al equipo ")
    else :
        print("El equipo no ha tenido suerte y no ha podido ganar aún ningún partido. Muchísima suerte a sus jugadores ")

lista_resultados1, puntos, cantidad_partidos = obtener_resultados()
racha_partidos(lista_resultados1)
print (f"El equipo ha conseguido {puntos} puntos en {cantidad_partidos} partidos. Felicidades a todos sus jugadores ")
