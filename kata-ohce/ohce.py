class Ohce:
    def __init__(self, nombre):
        self.nombre = nombre

    def procesar(self, entrada):
        invertido = entrada[::-1]
        if self.es_palindromo(entrada):
            return f"{invertido}\n¡Bonita palabra!"
        return invertido

    def es_palindromo(self, texto):
        return texto == texto[::-1]
