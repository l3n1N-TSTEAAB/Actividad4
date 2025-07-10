def Menu():
    print("MENU - FARMACIA")
    print("1. RECEPCION - CLIENTES")
    print("2. AGREGAR - MEDICAMENTOS")
    print("3. SALIR")


class Pacientes():
    def __init__(self, nombre, dpi, edad, padecimiento):
        self.__nombre = nombre
        self.__dpi = dpi
        self.__edad = edad
        self.__padecimiento = padecimiento


def get_paciente(self):
    return f"NOMBRE: {self.__nombre} DPI: {self.__dpi} EDAD: {self.__edad} PADECIMENTO: {self.__padecimento}"


opcion = 0
PilaPacientes = []
while opcion != 3:
    opcion = 0
    Menu()
    opcion = int(input("OPCION A ELEGIR: "))
    match (opcion):
        case 1:
            print("AGREGAR NUEVOS PACIENTES")
            nombre = input("NOMBRE: ")
            dpi = input("DPI: ")
            edad = input("EDAD: ")
            padecimiento = input("PADECIMENTO: ")
            pacienteNuevo = Pacientes(nombre, dpi, edad, padecimiento)
            PilaPacientes.append(pacienteNuevo)
        case 2:

