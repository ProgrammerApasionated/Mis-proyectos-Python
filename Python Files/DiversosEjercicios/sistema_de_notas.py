# def obtener_datos()                ->    Obtener la lista con los datos.

# def mostrar_info(lista)            ->    Enseñar toda la información de los estudiantes.

# def media_alumno(lista_num)        ->    Con las notas del primer estudiante calcula su media.

# def nota_maxima_minima(lista)      ->    Con la lista saca el valor máximo y mínimo.

# def encontrar_alumno (lista_datos) ->    Busca el nombre de un estudiante y muestra sus datos.



def obtener_datos():
    lista_datos = []
    nombre = input ("Introduce el nombre completo del estudiante :  \n")
    while nombre == "":
        nombre = input ("Nombre no válido, introduce un número válido : \n")
    lista_datos.append(nombre)
    notas = float (input ("Introduce cada nota individualmente (Introduce un valor no válido para acabar (0-10):   \n"))
    while notas < 0 or notas > 10:
        notas = float(input ("Dato incorrecto. Introduce la nota del 0 al 10: \n"))
    while 10 >= notas >= 0 :
        lista_datos.append(notas)
        notas = float (input("Introduce cada nota individualmente (Introduce un valor no válido para acabar (0-10):   \n"))
        if notas < 0 or notas > 10:
            break
    return lista_datos

def mostrar_info(lista):
    print(f"Estudiante: {lista[0]}")
    print("Notas:")
    for nota in lista[1:]:  #Notas del índice 1 hasta el final
        print(nota, end="  ")

def media_alumno(lista_num):
    media_persona = 0
    lista_num = lista_num[1:] # Todas las notas del estudiante
    for nota in range (len(lista_num)):
        if nota >= 0:
            media_persona += lista_num[nota]
    media_persona = media_persona / len(lista_num)
    if media_persona >= 5:
        print (f"\nEl estudiante ha tenido suerte y con su media de {media_persona} ha aprobado. ")
    else :
        print (f"\nEl estudiante no ha tenido suerte y con su media de {media_persona} ha suspendido. ")
    return media_persona

def nota_maxima_minima(lista): # Índice 1 primer número.
    nota_min = lista[1]
    nota_max = lista[1]
    for notas in range (len(lista)):
        if notas >= 1:
            if lista[notas] > nota_max:
                nota_max = lista[notas]
            if lista[notas] < nota_min:
                nota_min = lista[notas]
    print (f"La nota máxima del estudiante ha sido {nota_max}. Felicidades! \n")
    print (f"La peor nota ha sido {nota_min}. Muchos animos y a mejorar \n ")


def encontrar_alumno(lista_datos):
    nombre = input("Introduce el nombre de un estudiante a buscar: ")
    for alumno in lista_datos:
        if alumno[0].lower() == nombre.lower(): # Se pone alumno[0] porque se puede entender como una matriz, y la posición 0 se entiende como el nombre
            print (f"El estudiante encontrado tiene estas notas: ")
            mostrar_info(alumno)
            media_alumno(alumno)
            nota_maxima_minima(alumno)
            return True
    print ("Estudiante no encontrado")
    return False

estudiantes = []

while True :
    estudiantes.append(obtener_datos())
    continuacion = input ("Quieres continuar añadiendo estudiantes? (S/N) \n")
    if continuacion != "S" :
        break
for i in range (len(estudiantes)):
    mostrar_info(estudiantes[i])

