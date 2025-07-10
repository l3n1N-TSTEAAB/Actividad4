class Medicamento:
    def __init__(self, nombre, dosis, presentacion, receta_requerida):
        self.nombre = nombre
        self.dosis = dosis
        self.__presentacion = presentacion
        self.receta_requerida = receta_requerida

    def get_medicamento(self):
        receta = "Sí" if self.receta_requerida else "No"
        return (f"{self.nombre} | {self.dosis} | {self.presentacion} | "
                f"Receta: {receta}")

