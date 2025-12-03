def racha_numeros_negativos(num):
    inicio = 0
    inicio_mayor = -1
    final_mayor = -1
    longitud = 0
    longitud_mayor = 0
    i = 0
    while i < len(num):
        if num[i] < 0:
            if longitud == 0:
                inicio = i
            longitud += 1
        else:
            if longitud > longitud_mayor:
                longitud_mayor = longitud
                inicio_mayor = inicio
                final_mayor = i - 1
            longitud = 0
        i += 1
    if longitud > longitud_mayor:
        longitud_mayor = longitud
        inicio_mayor = inicio
        final_mayor = len(num) - 1
    if longitud_mayor > 0:
        print(f"La racha mayor de números negativos ha sido del índice {inicio_mayor} al {final_mayor} con {longitud_mayor} números")
    else:
        print("No hay números negativos")


lista = [-1, 2, -3, -3 , 4]
racha_numeros_negativos(lista)