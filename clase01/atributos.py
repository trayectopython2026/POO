""" 
    - class : permitir definir una clase 
    - Persona : nombre de la clase
    - nombre y edad : atributos
 """

class Persona:
    nombre= "Juan"
    edad = 25

""" 
    Instanciar la clase , para crear un objeto
    persona1: creando un objeto a partir de la clase Persona
"""
persona1  = Persona()

print(persona1.nombre)
print(persona1.edad)

""" Metodo Constructor """
""" 
    __init__ : metodo que inicializa los atributos de cada objeto cuando se crea
    self : referencia al objeto sobre el que se esta trabajando y llama a los atributos que yo cree
"""

class Persona:
    def __init__(self, nombre, edad):
         self.nombre = nombre
         self.edad = edad


""" instanciar  """

persona1 = Persona("Alejandro", 30)
persona2 = Persona("Ana", 21)

print(persona1.nombre, persona1.edad)
print(persona2.nombre, persona2.edad)

""" Modificar Atributos """
persona1.edad = 31

print(persona1.nombre,persona1.edad)

""" 
    01 - Crear una clase Animal
    Crear una clase con los atributos nombre y especie. Instanciar tres animales diferentes y mostrar sus datos
"""



""" 
    02- Crear una clase Auto
    Atributos: marca, modelo, año. 
    crear dos autos y mostrar sus caracteristicas
"""

print("*************************************")

class Auto:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    


# Crear instancia
auto1 = Auto("Ford", "Fiesta", 1998)
auto2 = Auto("Toyota" , "Corolla" , 2022)

# Mostrar caracteristicas
print("Auto 1")
print("Marca:" , auto1.marca)
print("Modelo:", auto1.modelo)
print("Año:" , auto1.anio)

print("*************************************")

print("Auto 2")
print("Marca:" , auto2.marca)
print("Modelo:", auto2.modelo)
print("Año:" , auto2.anio)





""" 
    03- Crear una clase alumno
    Atributos: nombre, apellido y nota
    Crear tres alumnos y modificar la nota de uno
"""

"""  
    04- Crear una clase videojuego
    Atributos: titulo, genero, plataforma y precio
    Crear 4 videojuegos y mostrar sus datos
"""

""" 
    05- Desafio integrador : Biblioteca
    crear una clase Libro con titulo , autor , año y disponibilidad . Crear 5 libros, mostrar sus datos y modificar la disponibilidad de 2.
"""







