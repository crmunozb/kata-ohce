class Ohce:
    def __init__(self, nombre):
        self.nombre = nombre

    def procesar(self, entrada):
        invertido = entrada[::-1]
        if entrada == entrada[::-1]:
            return f"{invertido}\n¡Bonita palabra!"
        return invertido

