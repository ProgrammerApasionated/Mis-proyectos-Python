# encontrar_palíndromo()  ->      Determina si un programa es un palíndromo o no.

# Inicializa una lista con la cantidad de palabras que son palíndromos, depura la cadena para no ser la vacía y evalúa si la cadena invertida es igual a la original.
# Al comprobar que es o no es igual, devuelve la solución y pide otra cadena, cuando el usuario introduzca una cadena vacía el programa rompe el bucle y enseña toda la información final.

# patron_concreto()       ->      Produce un patrón de carácteres concretos.

# Inicializamos una lista con las cadenas con los patrones, luego enseñamos al usuario la forma que tiene el patrón y luego calculamos la cadena y la mostramos.
# Añadimos a la lista el patrón hecho y luego con un bucle for conseguimos mostrar la cantidad de patrones conseguidos.


# eliminar_espacios()     ->      Elimina los espacios de una frase

# Inicializamos una lista con las cadenas sin los espacios vacíos, luego creamos e inicializamos una variable dentro del bucle while para que en cada interación cambie.
# Carácter a carácter ponemos la solución en esta nueva variable y posteriormente la guardamos en la lista y mostramos las frases guardadas en la lista.


# detectar_algo()         ->      Detecta un carácter en una frase

# Inicializamos una lista con la cantidad de carácteres que tiene de un carácter dado por el usuario, buscamos el patrón mediante índices con un bucle for y aumentamos la cantidad.
# Finalmente, depuramos que la frase dada para que no sea un conjunto vacío para luego repetir el bucle, y enseñamos una lista con cada interación y cantidad del patrón.


def encontrar_palindromo():
    lista_palindromos = []   # Inicializa una lista con la cantidad de palabras que son palíndromos.
    cadena = input ("Introduce la cadena \n")
    while cadena != "":
        cadena_invertida = ""   # Inicializa la cadena invertida con una cadena vacía.
        cadena = cadena.lower() # Pone los carácteres de la cadena en minúsculas.
        for i in range (len(cadena) - 1, -1 , -1):  # for i in range ( Start , Stop , Step )  -> cadena = " AzulVerde "  -> for i in range ( 8 , -1 , -1 ).
            cadena_invertida += cadena[i]           #
        if cadena_invertida == cadena :
            print (f"La cadena {cadena} es un palíndromo, {cadena} es igual a {cadena_invertida} ")
            lista_palindromos.append(cadena)        # Es palíndromo y lo añade a la lista.
        else :
            print (f"La cadena {cadena} no es un palíndromo, {cadena} no es igual a {cadena_invertida}")
        cadena = input ("Introduce la cadena \n")
    print(f"Has introducido {len(lista_palindromos)} secuencias de patrones ")  # len(lista_palindromos) = Cantidad de palíndromos.
    for i in range(len(lista_palindromos)):
        print(f"Palíndromo [{i+1}]  ->  {lista_palindromos[i]}")  # Enseña la lista con esta estructura [Número] -> Indice de la lista de palíndromos.

def patron_concreto():
    cadena = " "        # Entra obligatoriamente al bucle
    lista_patrones = [] # Lista con los patrones obtenidos
    while cadena != "": # Depuramos la cadena vacía
        cadena = input("Introduce la cadena \n")
        if cadena == "":
            break # ¿¿¿Para qué introducir el patrón si no hay cadena???
        patron = input("Introduce el patrón \n")
        repeticiones = int(input("Introduce las repeticiones del patrón \n"))
        cadena = cadena.title() # Puramente estético para verlo mejor -> cadena = azul  patrón = verde -> Azul Verde
        print (f"El patrón tendrá esta estructura {cadena} junto con {patron} multiplicado por {repeticiones}") # Ejemplo: cadena = Azul, patron = Verde, repeticiones = 3. -> Azul  Verde 3  -> AzulVerdeAzulVerdeAzulVerde = (AzulVerde) * 3.
        cadena_modificada = (cadena + patron) * repeticiones
        print (f"La cadena modificada tiene esta estructura {cadena_modificada} \n")
        lista_patrones.append(cadena_modificada)
    print(f"Has introducido {len(lista_patrones)} secuencias de patrones ")    #  -> len(lista_patrones) = Cantidad de patrones obtenidos.
    for i in range(len(lista_patrones)):
        print(f"Patrón generado [{i+1}] -> {lista_patrones[i]}")               # Enseña la lista con esta estructura [Número] -> Indice de la lista de patrones.

def eliminar_espacios():
    lista_depurada = [] # Inicializamos la lista con las frases depuradas
    frase_dada = input ("Introduzca una frase con espacios para eliminar los espacios \n")
    while frase_dada != "":                      # Frase no correcta, no entra.
        frase_correcta = ""
        frase_dada = frase_dada.title()          # Cuestión pura de estética.
        for i in range (len(frase_dada)):
            if frase_dada[i] != " ":
                frase_correcta += frase_dada[i]  # Obtenemos aquí la solución.
        lista_depurada.append(frase_correcta)
        frase_dada = input ("Introduzca una frase con espacios para eliminar los espacios \n")
    for i in range (len(lista_depurada)):
        print (f"Frase juntada [{i+1}] -> {lista_depurada[i]}") # Enseñamos la lista con las distintas frases con la depuración.

def detectar_algo():
    lista_depurada = [] # Lista con la cantidad del patrón
    frase_dada = input ("Introduzca una frase para encontrar un patrón en ella : \n")
    patron_a_buscar = input ("Introduce el patrón a buscar : \n")
    while len(patron_a_buscar) > 1 :  # No puede haber más de un patrón a buscar.
        patron_a_buscar = input ("Introduce un patrón correcto (un carácter concreto solo) \n")
    while frase_dada != "": # Frase distinta del conjunto vacío.
        frase_dada = frase_dada.lower()
        frase_perfecta = frase_dada.replace(" ", "")  # Patron automático de la función eliminar_espacios().
        cant_patron = 0
        for i in range (len(frase_perfecta)):
            if frase_perfecta[i] == patron_a_buscar:
                cant_patron += 1  # Aumenta la cantidad del patrón.
        lista_depurada.append(cant_patron)
        frase_dada = input("Introduce la frase : \n")
        if frase_dada == "":  # Frase no válida, no hace falta pedir el siguiente valor.
            break
        else:
            patron_a_buscar = input("Introduce el patrón a buscar : \n")
    i = 0
    while i < len(lista_depurada): # Forma alternativa del for para enseñar las distintas interacciones.
        print (f" [{i+1}] Se ha encontrado {lista_depurada[i]} veces ")  # [Número] Se han encontrado (índice de la lista) veces.
        i += 1

detectar_algo()