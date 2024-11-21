print(" ")# print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")# print imprime un espacio

class Persona: # abriendo clase
    def __init__(self, nombre='', edad=0, dni=''): # Constructor de la clase Persona que inicializa nombre, edad y dni 
        self.nombre = nombre# dando datos
        self.edad = edad# dando datos
        self.dni = dni# dando datos

    def mostrar(self):# Método para mostrar los detalles de la persona
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def esMayorDeEdad(self):# devuelve True si la persona es mayor de edad 
        return self.edad >= 18

persona = Persona("Ana", 30, "12345678A")# Crear una instancia de la clase Persona con nombre "Ana", edad 30 y dni "12345678A"

persona.mostrar() # Llamar al método mostrar para imprimir los detalles de la persona

print("Es mayor de edad:", persona.esMayorDeEdad()) # print imprime si la persona es mayor de edad o no

print(" ") # print imprime un espacio
