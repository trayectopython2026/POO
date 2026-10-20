""" Acciones """

class Perro:
    def __init__(self,nombre,raza,anio):
        self.nombre = nombre
        self.raza = raza
        self.anio = anio

    def ladrar(self):
        print(self.nombre, "Esta ladrando")

    def caracteristicas(self):
        print(f"El nombre del perro es {self.nombre} - la raza del perro es {self.raza} y tiene {self.anio} años")    

print("***************ACA finaliza la clase *********************")        

perro1 = Perro("Firulais","Dalmata", 5)
perro2 = Perro("Pepito", "Calle", 2)


# print(perro1.nombre, perro1.raza, perro1.anio)

perro1.ladrar()
perro1.caracteristicas()

print(perro2.nombre, perro2.raza, perro2.anio)

perro2.caracteristicas()
perro2.ladrar()

""" Ejemplo 2 : Metodos que modifican atributos """

class Cuenta:
     def __init__(self,titular , saldo):
         self.titular = titular
         self.saldo = saldo

     def depositar(self,cantidad):
         if cantidad > 0:
             # self.saldo = self.saldo + cantidad
             self.saldo += cantidad

     def mostrar_saldo(self):
         print(self.titular , "tiene Saldo: " , self.saldo)  

cuenta1 = Cuenta("Mariana", 1000)

print("Saldo Actual: ")
cuenta1.mostrar_saldo()
cuenta1.depositar(500)

print("Saldo actualizable: ")
cuenta1.mostrar_saldo()

cuenta1.depositar(1000)

print("Saldo actualizable 2: ")
cuenta1.mostrar_saldo()

cuenta2 = Cuenta("Martin", 10)

cuenta2.mostrar_saldo()

