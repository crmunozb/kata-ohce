class Ohce:
    def __init__(self, nombre, hora_actual=None):
        self.nombre = nombre
        self.hora_actual = hora_actual or self._hora_del_sistema

    def _hora_del_sistema(self):
        from datetime import datetime
        return datetime.now().hour

    def saludo(self):
        hora = self.hora_actual()
        if 6 <= hora < 12:
            return f"¡Buenos días, {self.nombre}!"
        elif 12 <= hora < 20:
            return f"¡Buenas tardes, {self.nombre}!"
        else:
            return f"¡Buenas noches, {self.nombre}!"
