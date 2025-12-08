class Libro:
    def __init__(self,nombre,isbn,autor,estado,genero):
        self.nombre   = nombre
        self.isbn     = isbn
        self.autor    = autor
        self.estado   = estado
        self.genero   = genero

    def __str__(self):
        return f"El libro se llama {self.nombre} con isb {self.isbn} autor {self.autor} y estado {self.estado}"

    def mostrar_datos(self):
        print (f"Nombre  -> {self.nombre}.")
        print (f"ISBN    -> {self.isbn}.")
        print (f"Autor   -> {self.autor}.")
        if self.estado:
            print ("Estado -> Prestado.")
        else:
            print ("Estado -> No Prestado.")
        print (f"Género  -> {self.genero}.")
        print("-" * 40)


    def mostrar_estado(self):
        if self.estado:
            print (f"El libro :")
            self.mostrar_datos()
            print ("Está prestado.")
        else:
            print(f"El libro : ")
            self.mostrar_datos()
            print ("No está prestado.")

    def prestar_libro(self):
        if self.estado:
            self.mostrar_datos()
            print ("El libro está prestado")
        else:
            self.estado = True
            self.mostrar_datos()
            print ("El libro se ha prestado correctamente.")

    def devolver_libro(self):
        if self.estado:
            self.estado = False
            self.mostrar_datos()
            print ("El libro se acaba de devolver. ")
        else:
            self.mostrar_datos()
            print("El libro no estaba prestado, no se puede devolver.")

class Biblioteca:

    def __init__ (self):
        self.libros = []

    def meter_libros(self,libro):
        for comprobar in self.libros:
            if comprobar.isbn == libro.isbn:
                print ("El libro ya está en la biblioteca")
                return
        self.libros.append(libro)
        print (f"El libro {libro.nombre} se ha añadido. ")


    def mostrar_libros(self):
        if not self.libros:
            print ("No hay libros en la biblioteca.")
            return
        else:
            for libro in self.libros:
                print (libro)
                print("-" * 40)


    def libro_nuevo(self):
        nombre = input ("Introduce el nombre del libro: \n")
        while nombre == "":
            nombre = input ("Introduce un nombre correcto. \n")
        isbn = input ("Introduce el isbn del libro, con 7 dígitos. \n")
        while len(isbn) != 7:
            isbn = input ("Introduce un isbn correcto. \n")
        estado = input ("Introduce el estado del libro, True/False. \n")
        while estado not in ("True", "False"):
            estado = input ("Introduce un estado correcto, True/False. \n")
        if estado == "True":
            estado = True
        else:
            estado = False
        autor = input ("Introduce el autor del libro: \n")
        while autor == "":
            autor = input ("Autor incorrecto.")
        genero = input ("Introduce el género del libro:  \n")
        while genero =="":
            genero = input ("Género incorrecto. \n")
        libro_creado = Libro (nombre, isbn, autor, estado, genero)
        return libro_creado

    def mostrar_libros_disponibles(self):
        if self.libros:
            for ejemplar in self.libros:
                if not ejemplar.estado:
                    ejemplar.mostrar_datos()
                    print ("-" * 40)
    def prestar_por_isbn(self):
        isbn = input ("Introduce el isbn del libro. (7 dígitos) \n")
        encontrado = False
        while len(isbn) != 7:
            isbn = input ("Introduce un isbn correcto. (7 dígitos) \n")
        for ejemplar in self.libros:
            if ejemplar.isbn == isbn:
                ejemplar.prestar_libro()
                encontrado = True
                break
        if not encontrado:
            print (f"El libro con isbn {isbn} no se ha encontrado. \n")

    def devolver_por_isbn(self):
        isbn = input("Introduce el isbn del libro. (7 dígitos) \n")
        encontrado = False
        while len(isbn) != 7:
            isbn = input("Introduce un isbn correcto. (7 dígitos) \n")
        for ejemplar in self.libros:
            if ejemplar.isbn == isbn:
                ejemplar.devolver_libro()
                encontrado = True
                break
        if not encontrado:
            print(f"El libro con isbn {isbn} no se ha encontrado. \n")

    def buscar_libro(self):
        opcion = input ("Dime con que parametro vas a buscar el libro, N = Nombre, I = ISBN, A = Autor")
        opcion = opcion.upper()
        encontrado = False
        if opcion == "N" :
            nom = input ("Introduce el nombre del libro. \n")
            while nom == "":
                nom = input ("Introduce el nombre correcto.")
            for ejemplar in self.libros:
                if ejemplar.nombre.lower() == nom.lower():
                    print ("El libro es : ")
                    ejemplar.mostrar_datos()
                    encontrado = True
                    break
            if not encontrado:
                print (f"El libro con {nom} como título no se ha encontrado")
        elif opcion == "I":
            isbn = input ("Introduce el isbn del libro. (7 dígitos) \n")
            while len(isbn) != 7:
                isbn = input ("Introduce el isbn correctamente. (7 dígitos) ")
            for ejemplar in self.libros:
                if ejemplar.isbn == isbn:
                    print ("El libro es : ")
                    ejemplar.mostrar_datos()
                    encontrado = True
                    break
            if not encontrado:
                print (f"No se ha encontrado libro con {isbn} como ISBN. ")
        elif opcion == "A" :
            aut = input ("Introduce el autor del libro. \n")
            while aut == "":
                aut = input ("Autor incorrecto. ")
            for ejemplar in self.libros:
                if ejemplar.autor == aut:
                    print ("El libro es : ")
                    ejemplar.mostrar_datos()
                    encontrado = True
                    break
            if not encontrado:
                print (f"No se ha encontrado libro con {aut} como autor. ")
        else:
            print ("Opción incorrecta. \n")

def menu():
    print ("-" * 30)
    print("1.-Crear un ejemplar y meterlo en la biblioteca : ")
    print("2.-Mostrar libros disponibles : ")
    print("3.-Buscar libro en la biblioteca: ")
    print("4.-Prestar un libro por su ISBN: ")
    print("5.-Mostrar libros de la biblioteca: ")
    print("6.-Devolver libro por su ISBN. ")
    print ("7.-Salir. ")
    print ("-" * 30)
    while True:
        opcion = input("Introduce la opción interesada: \n")
        if opcion.isdigit() and 1 <= int(opcion) <= 7:
            opcion = int(opcion)
            break
        print("Introduce un número válido entre 1 y 7.")
    if opcion == 1:
        print("Has elegido crear un ejemplar. \n")
        nuevo_libro = biblioteca.libro_nuevo()
        biblioteca.meter_libros(nuevo_libro)
        print("El nuevo libro se ha añadido en la biblioteca. \n")
        return True
    elif opcion == 2:
        print("Has elegido la opción 2. \n")
        biblioteca.mostrar_libros_disponibles()
        return True
    elif opcion == 3:
        print("Has elegido la opción 3. \n")
        biblioteca.buscar_libro()
        return True
    elif opcion == 4:
        print("Has elegido la opción 4. \n")
        biblioteca.prestar_por_isbn()
        return True
    elif opcion == 5:
        print("Has elegido la opción 5. \n")
        biblioteca.mostrar_libros()
        print("Estos son los libros que están actualmente en la biblioteca. \n")
        return True
    elif opcion == 6:
        print ("Has elegido la opción 6. \n")
        biblioteca.devolver_por_isbn()
        return True
    else:
        print ("Bye Bye. \n")
        return False


biblioteca = Biblioteca()

while menu():
    continue
