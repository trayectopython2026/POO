class Persona:
    """ Metodo constructor """
    def __init__(self, nombre , edad ):
           self.nombre = nombre
           self.edad = edad


persona1 = Persona("Alejandro", 30)
print(f"Mi nombre es: {persona1.nombre}")
print(f"Mi edad es: {persona1.edad}")

persona2 = Persona("Ana", 23)
print("Mi nombre es :", persona2.nombre)
print("Mi edad es: " , persona2.edad)

""" Modificar atributos """

persona1.nombre = "Ale"

print(f"Mi nombre es: {persona1.nombre}")


""" 
    01 - Crear una clase Animal
    Crear una clase con los atributos nombre y especie. Instanciar tres animales diferentes y mostrar sus datos
"""

print("*****************EJ1**************************")

class Animal:
      def __init__(self,nombre, especie):
            self.nombre = nombre
            self.especie = especie


animal1 = Animal("Firulais", "Perro")
animal2 = Animal("Michi", "Gato")
animal3 = Animal("Piolin", "Canario")

print(animal1.nombre, animal1.especie)
print(animal2.nombre, animal2.especie)
print(animal3.nombre, animal3.especie)




""" 
    02- Crear una clase Auto
    Atributos: marca, modelo, año. 
    crear dos autos y mostrar sus caracteristicas
"""


print("*****************EJ2**************************")

class Auto: 
      def __init__(self, marca, modelo, anio):
            self.marca = marca
            self.modelo = modelo
            self.anio = anio

auto1 = Auto("Ford", "Fiesta", 2018)
auto2 = Auto("Toyota", "Corolla", 2022)

print(f"Marca del auto {auto1.marca} , modelo del auto {auto1.modelo}, año del auto {auto1.anio}")

print(f"Marca del auto {auto2.marca} , modelo del auto {auto2.modelo}, año del auto {auto2.anio}")


""" 
    05- Desafio integrador : Biblioteca
    crear una clase Libro con titulo , autor , año y disponibilidad . Crear 5 libros, mostrar sus datos y modificar la disponibilidad de 2.
"""


class Libro:
      def __init__(self, titulo, autor, anio, disponible):
            self.titulo = titulo
            self.autor = autor
            self.anio = anio
            self.disponible = disponible


libro1 = Libro("El principito" , "Antonie de Saint-Exupery", 1943, True)
libro2 = Libro("1984" , "George Orwell", 1949, False)
libro3 = Libro("El Hobbit" ,"J.R.R Tolkien", 1937, True)

print(libro1.titulo, libro1.autor, libro1.anio, libro1.disponible)
print(libro2.titulo, libro2.autor, libro2.anio, libro2.disponible)
print(libro3.titulo, libro3.autor, libro3.anio, libro3.disponible)        

libro1.disponible= False
libro2.disponible = True

print("Disponibilidad actualizada")
print(libro1.titulo, libro1.autor, libro1.anio, "disponibilidad:", libro1.disponible)
print(libro2.titulo, libro2.autor, libro2.anio, "disponibilidad:",  libro2.disponible)