print(" ")# print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")# print imprime un espacio

class Cuenta: # abriendo clase
    def __init__(self, titular, cantidad=0.0): # Constructor de la clase Cuenta que inicializa titular y cantidad 
        if not titular: # Si no se proporciona un titular, lanza una excepción
            raise ValueError("El titular es obligatorio.")
        self.titular = titular# dando valores
        self.cantidad = cantidad# dando valores

    def mostrar(self):# Método para mostrar los detalles de la cuenta
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")

    def ingresar(self, cantidad): # Método para ingresar dinero a la cuenta
            self.cantidad += cantidad

    def retirar(self, cantidad):# Método para retirar dinero de la cuenta
        self.cantidad -= cantidad

cuenta = Cuenta("Ana")#  Cuenta "Ana" y cantidad inicial de 0.0
cuenta.mostrar()#  mostrar para imprimir los detalles de la cuenta

cuenta.ingresar(300)# Ingresar 300 unidades a la cuenta
cuenta.mostrar()# Mostrar los detalles de la cuenta después del ingreso

cuenta.retirar(100)# Retirar 100 unidades de la cuenta
cuenta.mostrar()# Mostrar los detalles de la cuenta después del retiro

cuenta.retirar(500) # Retirar 500 unidades de la cuenta, lo que llevará el saldo a números rojos
cuenta.mostrar()# Mostrar los detalles de la cuenta después del retiro

print(" ")# print imprime un espacio