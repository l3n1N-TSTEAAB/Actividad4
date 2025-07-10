class Medicamento:
    def __init__(self, nombre, dosis, presentacion, receta_requerida, precio):
        self.__nombre = nombre
        self.__dosis = dosis
        self.__presentacion = presentacion
        self.__receta_requerida = receta_requerida
        self.__precio = precio

    def get_medicamento(self):
        return f"Medicamento: {self.__nombre} Dosis: {self.__dosis} Presentacion: {self.__presentacion}, Con receta: {self.__receta_requerida} Precio: {self.__precio}"

def agregarmedicamento():
