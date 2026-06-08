class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"hola mi nombre es {self.nombre} y tengo {self.edad} años.")

    def es_mayor_de_edad(self):
        return self.edad >= 18



persona1 = Persona("Daniella", 22)
persona1 .presentarse()

if persona1.es_mayor_de_edad():
    print("es mayor de edad")
else:
    print("es menor de edad")