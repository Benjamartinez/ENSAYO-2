import csv
import os
from datetime import datetime

def menu():
    print("1.- Registrar nueva bitácora")
    print("2.- Listar bitácoras realizadas")
    print("3.- Exportar bitácoras")
    print("4.- Salir del sistema")
    opcion = input("Seleccione una opción: ")
    return opcion