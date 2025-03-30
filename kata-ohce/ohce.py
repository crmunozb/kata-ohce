from datetime import datetime

class Ohce:
    def __init__(self, nombre, hora_actual=None):
        self.nombre = nombre
        self.hora_actual = hora_actual or self._hora_del_sistema

    def _hora_del_sistema(self):
        return datetime.now().hour

    def saludo(self):
        hora = self.hora_actual()
        if 6 <= hora < 12:
            return f"¡Buenos días, {self.nombre}!"
        elif 12 <= hora < 20:
            return f"¡Buenas tardes, {self.nombre}!"
        else:
            return f"¡Buenas noches, {self.nombre}!"

    def es_palindromo(self, texto):
        return texto == texto[::-1]

    def procesar(self, entrada):
        saludo = self.saludo()
        invertido = entrada[::-1]

        if self.es_palindromo(entrada):
            return f"{saludo}\n{invertido}\n¡Bonita palabra!"

        return f"{saludo}\n{invertido}"
