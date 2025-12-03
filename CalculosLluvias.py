# def obtener_lluvias()                ->  Obtiene una lista con la cantidad de lluvia.

# def lluvia_maxima(lista_lluvias)     ->  Obtiene el valor máximo de una lista.

# def lluvia_minimo(lista_lluvias)     ->  Obtiene el valor mínimo de una lista.

# def dias_sin_lluvia(lista_lluvias)   ->  Obtiene la cantidad de dias sin lluvia.

# def racha_de_lluvias(lista_lluvias)  ->  Obtiene la cantidad máxima de rachas de lluvias.




def obtener_lluvias():
    lista_lluvias = []
    cadena = input ("Introduce la cantidad de lluvia en (mm) (Cadena vacía para acabar) : \n")
    while cadena != "" :
        lista_lluvias.append(int(cadena))
        cadena = input ("Introduce la cantidad de lluvia en (mm) (Cadena vacía para acabar) : \n")
    return lista_lluvias

def lluvia_maxima(lista_lluvias):
    max_lluvias = lista_lluvias[0]
    for maximo in lista_lluvias :
        if maximo > max_lluvias :
            max_lluvias = maximo
    return max_lluvias

def lluvias_minimas(lista_lluvias):
    min_lluvias = lista_lluvias [0]
    for minimo in lista_lluvias:
        if minimo < min_lluvias:
            min_lluvias = minimo
    return min_lluvias

def dias_sin_lluvia(lista_lluvias):
    cantidad_dias = 0
    for cantidad in lista_lluvias:
        if cantidad == 0:
            cantidad_dias += 1
    return cantidad_dias

def racha_de_lluvias(lista_lluvias):
    inicio = -1
    longitud = 0
    mayor_inicio = -1
    mayor_longitud = 0
    mayor_final = -1
    i = 0
    while i < len(lista_lluvias):
        if lista_lluvias[i] > 0:
            if longitud == 0:
                inicio = i
            longitud += 1
        else:
            if longitud > mayor_longitud:
                mayor_longitud = longitud
                mayor_inicio = inicio
                mayor_final = i - 1
            longitud = 0
        i += 1
    if longitud > mayor_longitud:
        mayor_longitud = longitud
        mayor_inicio = inicio
        mayor_final = i - 1
    print(f"La racha de lluvias mayor ha sido de {mayor_longitud} dias \n")
    print(f"Ha empezado del dia {mayor_inicio} al dia {mayor_final} \n")

lista1_lluvias = obtener_lluvias()
cantidad_lluvia_maxima = lluvia_maxima(lista1_lluvias)
cantidad_lluvia_minima = lluvias_minimas(lista1_lluvias)
cant_no_lluvia = dias_sin_lluvia(lista1_lluvias)
print (f"El día con la máxima lluvia ha sido {cantidad_lluvia_maxima} mm  y de menos {cantidad_lluvia_minima} mm \n")
print (f"La racha con menos lluvias ha sido de {cant_no_lluvia} dias \n")
racha_de_lluvias(lista1_lluvias)
