class Perro:
     def __init__ (self, nombre):
          self.nombre = nombre

     def ladrar(self):
          print(self.nombre, "esta ladrando")


perro = Perro("Firulais")

perro.ladrar()

""" 
    Metodos que modifican atributos
"""

class Cuenta:
    def __init__(self, titular , saldo):
          self.titular = titular
          self.saldo = saldo
     
    def depositar(self, cantidad):
         if cantidad > 0:
           # self.saldo = self.saldo + cantidad
            self.saldo += cantidad

    def mostrar(self):
         print(self.titular , "tiene un saldo de :", self.saldo)

cuenta1 = Cuenta("Juan", 1000)
cuenta1.mostrar()
cuenta1.depositar(500)
cuenta1.mostrar()

""" 
    Metodos con return

"""

class Rectangulo: 
     def __init__(self, base , altura):
          self.base = base
          self.altura = altura

     def calcular_area(self):
          return self.base * self.altura

figura1 = Rectangulo(5,3)

print("Area del rectangulo: " , figura1.calcular_area())
          
""" 
    01- Clase Calculadora
    Crear Metodos para sumar, restar , multiplicar y dividir, Controla que no se dividda por cero
"""

class Calculadora:
     def __init__(self,num1, num2):
          self.num1 = num1
          self.num2 = num2

     def sumar(self):
          return self.num1 + self.num2
     
     def restar(self):
          return self.num1 - self.num2

     def multiplicar(self):
               return self.num1 * self.num2

     def dividir(self):
          if self.num2 != 0:
               return self.num1 / self.num2
          else:
               return "no se puede dividir por cero"
                   

numeros = Calculadora(2,2)

print("la suma es: " , numeros.sumar())
print("la restar es: " , numeros.restar())
print("la multiplicar es: " , numeros.multiplicar())
print("la dividir es: " , numeros.dividir())


""" 
    Ej:02 - Clase Alumno

    Atributos: nombre y nota
    un metodo para ver si aprobo o no, +  6 se aprueba 
    crear 3 alumnos minimo
"""

class Alumno:
     def __init__(self,nombre, nota):
          self.nombre = nombre
          self.nota = nota

     def aprobo(self):
          if self.nota > 6:
               return "Aprobo"
          else:
               return "No Aprobo"


alumno1 = Alumno("Juan", 8)
alumno2 = Alumno("Maria", 4)
alumno3 = Alumno("Pedro", 6)

print(alumno1.nombre, alumno1.aprobo())
print(alumno2.nombre, alumno2.aprobo())
print(alumno3.nombre, alumno3.aprobo())






""" EJ.:  03
    Clase producto
    Atributos: nombre, precio y stock
    Crear Metodos para vender unidades, reponer stock y consultar cantidad disponible

 """

print("*********************EJ 03 - Productos********************************")

class Producto:

     def __init__(self, nombre, precio, stock):
          self.nombre = nombre
          self.precio = precio
          self.stock = stock

     # vender producto
     def vender(self, cantidad):
          if cantidad <= 0:
               print("La cantidad debe ser mayor a cero")
          elif cantidad > self.stock:
               print("No hay suficiente stock")
          else:
               self.stock -= cantidad
               print("Venta realizada")

     # reponer producto
     def reponer(self, cantidad):
          if cantidad > 0:
               self.stock += cantidad 
               print("Stock actualizado")
          else:
               print("Cantidad incorrecta")

     # consultar el stock
     def consultar_stock(self):
          return self.stock


producto1 = Producto("Mouse", 1500, 10)

print("Producto:" ,  producto1.nombre )
print("Precio:" , producto1.precio)
print("Stock inicial: ", producto1.consultar_stock())

print("***************Vendemos 3 unidades***************************")
producto1.vender(3)

print("Stock Actual: ", producto1.consultar_stock())
          
print("***************Reponer  5 unidades***************************")     

producto1.reponer(7)

print("Stock Actual: ", producto1.consultar_stock())


print("***************Intentamos vender 20 unidades***************************")  

producto1.vender(20)
print("Stock final: ", producto1.consultar_stock())



