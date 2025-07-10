class Medicamento:
    def __init__(self, nombre, dosis, presentacion, receta_requerida, precio):
        self.__nombre = nombre
        self.__dosis = dosis
        self.__presentacion = presentacion
        self.__receta_requerida = receta_requerida
        self.__precio = precio

    def get_medicamento(self):
        return f"Medicamento: {self.__nombre} Dosis: {self.__dosis} Presentacion: {self.__presentacion}, Con receta: {self.__receta_requerida} Precio: {self.__precio}"

listaMedicamentos = []

def agregarMedicamento():
    nombre = input("Ingresa el nombre del medicamento: ")
    while True:
        try:
            dosis = int(input("Ingresa la dosis del medicamento (gramos): "))
            break
        except ValueError:
            print("El valor es incorrecto")
    presentacion = input("Ingresa la presentacion del medicamento: ")
    receta_requerida = input("El medicamento requiere receta medica?(Si,No): ")
    while True:
        try:
            precio = int(input("Ingresa la precio del medicamento: "))
            break
        except ValueError:
            print("El valor es incorrecto")

    nuevoMedicamento = Medicamento(nombre, dosis, presentacion, receta_requerida, precio)
    listaMedicamentos.append(nuevoMedicamento)

def mostrarMedicamentos():
    for medicamento in listaMedicamentos:
        print(medicamento.get_medicamento())
