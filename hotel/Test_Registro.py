from .models import TestInsert_1

class Registro_Test1():
    
    def guardarEnDB(nombre, categoria, edad):
        insercion_registro_test = TestInsert_1(nombre_usuario_test = nombre, categoria_test = categoria, edad_test = edad)
        insercion_registro_test.save()
        print("Registro Guadrado")