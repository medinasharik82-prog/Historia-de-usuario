from datetime import datetime

class RegistroControl:
    def _init_(self, vehiculo, chofer):
        self.vehiculo = vehiculo
        self.chofer = chofer
        self.fecha_entrada = datetime.now().strftime("%H:%M:%S")
        self.fecha_salida = None

    def marcar_salida(self):
        self.fecha_salida = datetime.now().strftime("%H:%M:%S")
