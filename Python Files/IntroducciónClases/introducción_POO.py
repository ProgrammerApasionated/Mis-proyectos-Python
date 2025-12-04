class Estudiante:

    def __init__ (self,nombre,notas,genero):
        self.nombre      = nombre
        self.notas       = notas
        self.genero      = genero

    def __str__ (self):
        return f"El nombre es {self.nombre}, sus nota/s son {self.notas} y su género es {self.genero} \n"


    def mostrar_informacion(self):
        print (f"Nombre -> {self.nombre}")
        print (f"Notas -> ", end="")
        for nota in self.notas:
            print (nota, end= " ")
        print (f"\nGénero -> {self.genero}")

    def mostrar_notas(self):
        i = 1  # Número de la nota
        for nota in self.notas:
            #print (f"La asignatura número [{i}] tiene como calificación {nota}")
            print (f"La asignatura [{i}] -> {nota}", end = ". \n")
            i += 1

    def media_notas(self):
        media = 0
        for nota in self.notas:
            media += nota
        media = media / len(self.notas)
        print (f"La media del estudiante {self.nombre} tiene una media de {media} puntos")

    def nota_pico(self):
        nota_max = self.notas[0]
        nota_min = self.notas[0]
        for nota in self.notas:
            if nota > nota_max:
                nota_max = nota
            elif nota < nota_min:
                nota_min = nota
        print (f"El estudiante {self.nombre} tiene un máximo de {nota_max} y un mínimo de {nota_min}")

    def cantidad_notas(self):
        cant_suspensos      = 0
        cant_suficientes    = 0
        cant_bienes         = 0
        cant_notables       = 0
        cant_sobresalientes = 0
        for nota in self.notas:
            if nota < 5:
                cant_suspensos += 1
            elif 5 <= nota < 6:
                cant_suficientes += 1
            elif 6 <= nota < 7:
                cant_bienes += 1
            elif 7 <= nota < 9:
                cant_notables += 1
            else:
                cant_sobresalientes += 1
        print (f"El estudiante {self.nombre} tiene {cant_suspensos} suspensos, {cant_suficientes} suficientes, {cant_bienes} bienes, {cant_notables} notables y {cant_sobresalientes} sobresalientes. \n")

    def cambiar_algo(self):
        opcion = input ("Quieres cambiar algún dato? (S/N) ")
        if opcion == "S":
            cambio = input ("Que quieres cambiar? (N = Nombre, NN = Notas y G = Genero. \n")
            if cambio == "N":
                nombre = input ("Introduce el nombre del estudiante cambiado. \n")
                while nombre == "" :
                    nombre = input ("Nombre incorrecto, cambia el nombre. \n")
                self.nombre = nombre
                print (f"El nombre se ha cambiado a {self.nombre}")
            elif cambio == "NN":
                notas = int (input ("Introduce notas válidas, de 10-0. \n"))
                lista_notas = []
                while notas < 0 or notas > 10:
                    notas = int (input ("Nota no válida, de 10-0. \n"))
                while 0 <= notas <= 10:
                    lista_notas.append(notas)
                    notas = int (input ("Introduce notas válidas, de 10-0 o no para acabar. \n"))
                self.notas = lista_notas
                print (f"Las notas se han cambiado a {self.notas}")
            elif cambio == "G":
                genero = input ("Introduce el genero del estudiante, (Hombre/Mujer). \n")
                while not (genero == "Hombre" or genero =="Mujer"):
                    genero = input ("Género incorrecto, cambia el género (Hombre/Mujer). \n")
                self.genero = genero
                print (f"El género se ha cambiado a {self.genero}")
        else:
            print ("No ha cambiado nada del estudiante. \n")

def creacion_estudiantes():
    nombre = input ("Introduce el nombre del nuevo estudiante. \n")
    while nombre == "":
        nombre = input ("Nombre incorrecto, introduce el nombre \n")
    notas = int(input("Introduce notas válidas, de 10-0. \n"))
    lista_notas = []
    while notas < 0 or notas > 10:
        notas = int(input("Nota no válida, de 10-0. \n"))
    while 0 <= notas <= 10:
        lista_notas.append(notas)
        notas = int(input("Introduce notas válidas, de 10-0, o una nota no válida para terminar. \n"))
    genero = input("Introduce el genero del estudiante, (Hombre/Mujer). \n")
    while not (genero == "Hombre" or genero == "Mujer"):
        genero = input("Género incorrecto, cambia el género (Hombre/Mujer). \n")
    return Estudiante (nombre,lista_notas,genero)

# EJEMPLOS DE USO #

#Estudiante_prueba = Estudiante ("Alberto",[1,2,3,4,5],"Hombre")
#print (Estudiante_prueba)
#Estudiante_prueba.mostrar_notas()
#Estudiante_prueba.cantidad_notas()
#Estudiante_prueba.cambiar_algo()
#nuevo = nuevo_estudiante()
#nuevo.mostrar_informacion()