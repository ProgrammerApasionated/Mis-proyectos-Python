# def obtener_notas ()                ->     Obtención de las notas de un usuario.

# def obtener_media (lista_notas)     ->     Obtención de la media de las notas.

# def racha_aprobados (lista_notas)   ->     Obtención de la racha de aprobados.

# def tipo_estudiante(lista_notas)    ->     Dependiendo de la media y la racha determinamos el tipo de estudiante.

# def enseñar_notas()                 ->     Con una lista con la asignatura y la nota enseñamos la información al usuario.


def obtener_notas():
    notas = []
    cadena = 1
    while  0 <= cadena  <= 10 :
        cadena = float(input("Introduce una nota válida (Del 0 al 10):  \n"))
        if 0 > cadena or cadena > 10 :
            break
        else:
            notas.append(cadena)
        print (notas)
    return notas

def obtener_media(nota):
    media = 0
    for cada_nota in nota:
        media += cada_nota
    media = media / len(nota)
    return media

def racha_aprobados(nota):
    inicio = 0
    final = -1
    longitud = 0
    max_inicio = -1
    max_longitud = 0
    i = 0
    while i < len(nota):
        if nota[i] >= 5:
            if inicio == 0:
                inicio = i
            longitud += 1
            final = i + 1
            i += 1
        else:
            if longitud > max_longitud:
                max_inicio = inicio
                max_longitud = longitud
                final = i + 1
            longitud = 0
            i += 1
    if longitud > max_longitud:
        max_inicio = inicio
        max_longitud = longitud
    # Tenemos el inicio de la racha más alta y el final también pero no lo utilizamos
    return max_longitud


def tipo_estudiante(notas):
    media_estudiante = obtener_media(notas)
    racha_alta = racha_aprobados(notas)
    if media_estudiante < 5 and racha_alta >= 1:
        print (f"El estudiante tiene notas regulares con una media de {media_estudiante} y una racha de hasta {racha_alta} aprobado/s")
    elif media_estudiante < 6 and racha_alta >=5 :
        print (f"El estudiante tiene notas buenas con una media de {media_estudiante} y una racha de hasta {racha_alta} aprobados, con una constancia alta")
    if media_estudiante >= 9 and racha_alta == len(notas):
        print (f"El estudiante tiene notas increíbles con uan media de {media_estudiante} y un racha perfecta de {racha_alta} aprobados")

def enseñar_notas():
    lista_todo = []
    asignatura = input("Introduce la asignatura que has tenido examen: \n ")
    nota       = int (input ("Introduce la nota de la asignatura : \n"))
    while asignatura != ""  and  0 <= nota <= 10 :
        lista_todo.append(asignatura)
        lista_todo.append(nota)
        asignatura = input("Introduce la asignatura que has tenido examen: \n ")
        if asignatura == "":
            break
        nota = int(input("Introduce la nota de la asignatura : \n"))
        if not(0 <= nota <= 10):
            break

    for i in range (len(lista_todo)):
        if (i+1) % 2 != 0 :  # Si la posición es impar entra
            print (f"Nota de la asignatura [{lista_todo[i]}] es de [{lista_todo[i+1]}]") # Posición impar -> i (Asignatura) y Posición par -> i + 1 (Nota)

enseñar_notas()

