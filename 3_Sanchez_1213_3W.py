print(" ")# print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")# print imprime un espacio

class Cuenta:# abriemdo clase
    def __init__(self, titular, cantidad=0.0):# Constructor de la clase Cuenta
        self.titular = titular  # dando valores
        self.cantidad = cantidad  # dando valores

    def ingresar(self, cantidad):# Constructor de la clase Cuenta 
        if cantidad > 0:  # Verifica si la cantidad a ingresar es positiva
            self.cantidad += cantidad  # Añade la cantidad al atributo cantidad

    def retirar(self, cantidad):# Método para retirar una cantidad de dinero de la cuenta
        self.cantidad -= cantidad  # Resta la cantidad del atributo cantidad

    def mostrar(self):# Método para mostrar los detalles de la cuenta
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")  # Imprime el titular y la cantidad con dos decimales

class CuentaJoven(Cuenta):# abriemdo clase
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0): # Constructor de la clase CuentaJoven
        super().__init__(titular, cantidad)  # Llama al constructor de la clase 
        self.bonificacion = bonificacion  # Asigna el valor del parámetro 

    def esTitularValido(self):# Método para verificar si el titular es válido 
        return 18 <= self.cantidad < 25  # Devuelve True si la cantidad está entre 18 y 25 

    def retirar(self, cantidad):# Método para retirar una cantidad de dinero de la cuenta si el titular es válido
        if self.esTitularValido():  # Verifica si el titular es válido
            super().retirar(cantidad)  # Llama al método retirar de la clase base Cuenta
        else:
            print("No se puede retirar dinero: el titular no es válido.")  # Imprime un mensaje si el titular no es válido

    def mostrar(self): # Método para mostrar  detalles de la cuenta 
        print(f"Cuenta Joven - Titular: {self.titular}, Cantidad: {self.cantidad:.2f}, Bonificación: {self.bonificacion}%")  # Imprime el titular, la cantidad y la bonificación

cuenta_joven = CuentaJoven("Ana", cantidad=20, bonificacion=10)#  titular "Ana", cantidad 20 y bonificación 10
cuenta_joven.mostrar()  # Llama al método mostrar para imprimir los detalles de la cuenta joven

cuenta_joven.ingresar(100)# Ingresar 100 unidades a la cuenta joven
cuenta_joven.mostrar()  # print imprime los detalles de la cuenta joven después del ingreso

cuenta_joven.retirar(50)# Retirar 50 unidades 
cuenta_joven.mostrar()  # print imprime detalles de la cuenta joven después del retiro

cuenta_joven.cantidad = 30  # Asigna directamente el valor 30 
cuenta_joven.retirar(50)  #  retirar 50 unidades

print(" ")# print imprime un espacio