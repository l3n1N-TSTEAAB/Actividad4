def Menu():
    print("MENU - FARMACIA")
    print("1. RECEPCION - CLIENTES")
    print("2. AGREGAR - MEDICAMENTOS")
    print("3. SALIR")
def MenuPacientes():
    print("MENU - PACIENTES")
    print("1. REGISTRAR NUEVO CLIENTE")
    print("2. ATENDER PACIENTE")
    print("3. MOSTRAR PACIENTE")
    print("4. REGRESAR AL MENU")

def MenuMed():
    print("MENU - MEDICAMENTO")
    print("1. REGISTRAR NUEVO MEDICAMENTO")
    print("2. ENTREGAR MEDICAMENTO")
    print("3. MOSTRAR MEDICAMENTOS")
    print("4. REGRESAR AL MENU")

class Pacientes():
    def __init__(self, nombre, dpi, edad, padecimiento):
        self.__nombre = nombre
        self.__dpi = dpi
        self.__edad = edad
        self.__padecimiento = padecimiento


def get_paciente(self):
    return f"NOMBRE: {self.__nombre} DPI: {self.__dpi} EDAD: {self.__edad} PADECIMENTO: {self.__padecimento}"


opcion = 0
opcion2 = 0
PilaPacientes = []
while opcion != 3:
    opcion = 0
    Menu()
    opcion = int(input("OPCION A ELEGIR: "))
    match (opcion):
        case 1:
            while(opcion2 !=4):
              opcion = 0
              MenuPacientes()
            opcion2 = int(input("OPCION A ELEGIR: "))
            match (opcion2):
                case 1:
                   print("AGREGAR NUEVOS PACIENTES")
                   nombre = input("NOMBRE: ")
                   dpi = input("DPI: ")
                   edad = input("EDAD: ")
                   padecimiento = input("PADECIMENTO: ")
                   pacienteNuevo = Pacientes(nombre, dpi, edad, padecimiento)
                   PilaPacientes.append(pacienteNuevo)
                case 2:
                   print("ATENDER PACIENTES")
                   PilaPacientes.remove(0)

                case 3:
                   print("MOSTRAR PACIENTES")
                   for paciente in PilaPacientes:
                     print(paciente.get_paciente())
        case 2:
            opcionM = 0
            MenuMed()
            opcionM = int(input("OPCION A ELEGIR: "))
            match (opcionM):
                case 1:
                    agregar_medicamento()
                case 2:
                    entregar_medicamento()
                case 3:
                    mostrar_medicamentos()






