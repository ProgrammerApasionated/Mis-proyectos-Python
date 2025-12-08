# obtener_lista_temperaturas()   ->     Obtiene una lista a partir de una cadena del usuario.

# Inicializa una lista con las temperaturas y pide las temperaturas, que posteriormente añade en la lista.

# eliminar_un_elemento()        ->      Mediante una lista de temperaturas borra un elemento.

# Pide un valor en pantalla, que si está en la lista pide confirmación y lo borra.
# Mediante un uso de un bucle while, se recorre la cadena buscando dicho elemento.

# media_temperaturas()          ->       Con una lista de temperaturas saca la media

# Inicializando una variable con la suma total de elementos posteriormente se recorre la lista y se obtiene la media.

# minima/maxima_temperatura()    ->      Calcula la máxima o mínima temperatura de una lista de temperaturas.

# Suponemos que el primer elemento es el máximo/mínimo y luego lo comparamos con todos los elementos de la lista.
# Con el elemento máximo/mínimo luego se devuelve.

# racha_de_ola_de_frio()        ->         Mediante una lista de temperaturas determina la cantidad de rachas de días que hacía temperatura negativa.

# Inicializamos las variables con las que trabajamos y mediante una estructura while comprobamos la condición.
# Posteriormente cambiamos las referencias de las variables y para asegurar la racha más alta cuando sale del bucle.
# Volvemos a hacer la comparación y dependiendo de la longitud enseñamos un mensaje u otro.



def obtener_lista_temperaturas():
    lista_temperaturas =[]
    cadena = input ("Introduce la temperatura necesitada : ")
    while cadena != "":
        lista_temperaturas.append(int(cadena))
        cadena = input("Introduce la temperatura necesitada : ")
    print (lista_temperaturas)
    return lista_temperaturas
def eliminar_un_elemento(lista_temperaturas):
    valor = int (input ("Introduce el valor a borrar  "))
    i = 0
    while i < len(lista_temperaturas):
        if lista_temperaturas[i] == valor :
            opcion = input (f"Quieres que elimine el valor {valor} (S/N) ")
            if opcion == "S":
                lista_temperaturas.remove(valor)
                print (f"La lista modificada ha quedado así {lista_temperaturas}")
            else :
                print (f"El elemento {valor} no se ha eliminado de la lista de temperaturas ")
        i += 1
    return lista_temperaturas

# Inicializar la lista, comprobar la cadena, añadir el elemento como número y hacer un return con la lista.

def media_temperaturas(listas_temperaturas):
    suma_total_temperaturas = 0
    for temperaturas in listas_temperaturas:
        suma_total_temperaturas += temperaturas
    media_total = suma_total_temperaturas / len(listas_temperaturas)
    return media_total

# Inicializa una variable que contiene el sumatorio de los elementos de la lista y luego calcula la media.

def maxima_temperatura(lista_temperaturas):
    temperatura_maxima = lista_temperaturas[0]
    for maxima in lista_temperaturas:
        if maxima > temperatura_maxima:
            temperatura_maxima = maxima
    return temperatura_maxima

# Supone el máximo como el primer índice de la lista y posteriormente evalúa los elementos de la lista.

def minima_temperatura(lista_temperaturas):
    temperatura_minima = lista_temperaturas[0]
    for minima in lista_temperaturas:
        if minima < temperatura_minima:
            temperatura_minima = minima
    return temperatura_minima

# Supone el mínimo como el primer índice de la lista y posteriormente evalúa los elementos de la lista.

def temperaturas_negativas(lista_temperaturas):
    lista_temperaturas_negativas = []
    for negativa in lista_temperaturas:
        if negativa < 0:
            lista_temperaturas_negativas.append(negativa)
    return lista_temperaturas_negativas

# Inicializa una variable con la solución y evalúa la condición para luego añadirla en la variable.

def racha_de_ola_de_frio(lista_temperaturas):
    inicio = -1
    longitud = 0
    mayor_inicio = -1
    mayor_longitud = 0
    mayor_final = -1
    i = 0
    while i < len(lista_temperaturas):
        if lista_temperaturas[i] < 0:
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
        print(f"La ola de frio ha durado {mayor_longitud} dias")
        print(f"Ha empezado del dia {mayor_inicio} al dia {mayor_final}")
    elif longitud > 0 :
        print(f"La ola de frio ha durado {mayor_longitud} dias")
        print(f"Ha empezado del dia {mayor_inicio} al dia {mayor_final}")
    else:
        print ("No ha habido una ola de frio")


# Algoritmo consistente en inicializar las variables + ir sumando índices para comprobar todos los valores.
# Finalmente, se depura los resultados y se enseña lo que significan.

## EJEMPLOS DE USO ##
''' 
lista_temperatura = obtener_lista_temperaturas()
maximo = maxima_temperatura(lista_temperatura)
minimo = minima_temperatura(lista_temperatura)
lista_temperatura_neg = temperaturas_negativas(lista_temperatura)
print (f"La lista de temperaturas es {lista_temperatura}")
print (f"La lista de temperaturas negativas es {lista_temperatura_neg}")
print (f"El valor más alto ha sido {maximo} grados ")
print (f"El valor más bajo ha sido {minimo} grados ")
racha_de_ola_de_frio(lista_temperatura)
eliminar_un_elemento(lista_temperatura)
media = media_temperaturas(lista_temperatura)
print (f"La media de {lista_temperatura} es {media} grados ") '''
