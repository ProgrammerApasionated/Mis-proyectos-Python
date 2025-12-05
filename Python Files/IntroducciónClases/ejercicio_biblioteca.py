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
            print ("El libro : ")
            self.mostrar_datos()
            print ("Ya está prestado y no se puede presentar.")
        else:
            self.estado = True
            print ("El libro : ")
            self.mostrar_datos()
            print ("Se acaba de prestar.")


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
    def prestar_por_isbn(self):
        isbn = input ("Introduce el isbn del libro. (7 dígitos) \n")
        encontrado = False
        while len(isbn) != 7:
            isbn = input ("Introduce un isbn correcto. (7 dígitos) ")
        for ejemplar in self.libros:
            if ejemplar.isbn == isbn:
                ejemplar.prestar_libro()
                encontrado = True
                break
        if not encontrado:
            print (f"El libro con isbn {isbn} no se ha encontrado")



    def buscar_libro(self):
        opcion = input ("Dime con que parametro vas a buscar el libro, N = Nombre, I = ISBN, A = Autor")
        opcion = opcion.upper()
        encontrado = False
        if opcion == "N" :
            nom = input ("Introduce el nombre del libro. \n")
            while nom == "":
                nom = input ("Introduce el nombre correcto.")
            for ejemplar in self.libros:
                if ejemplar.nombre == nom:
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


libro1 = Libro("AzulVerde", "1234567", "Hannah Grace", False, "Romance")
libro2 = Libro("Matemáticas Avanzadas", "2345678", "Alan Turing", False, "Ciencia")
libro3 = Libro("El Quijote", "3456789", "Miguel de Cervantes", True, "Novela")
libro4 = Libro("Física Cuántica", "4567890", "Albert Einstein", False, "Ciencia")
Biblio1 = Biblioteca ()
Biblio1.meter_libros(libro1)
Biblio1.meter_libros(libro2)
Biblio1.meter_libros(libro3)
Biblio1.meter_libros(libro4)
Biblio1.mostrar_libros()