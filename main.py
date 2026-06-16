from datetime import datetime

# --- CLASES ---
class Vehiculo:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo

class Chofer:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre

class RegistroControl:
    def __init__(self, vehiculo, chofer):
        self.vehiculo = vehiculo
        self.chofer = chofer
        self.fecha_entrada = datetime.now().strftime("%H:%M:%S")

    def mostrar(self):
        return (
            f"Hora: {self.fecha_entrada} | "
            f"Placa: {self.vehiculo.placa} | "
            f"Modelo: {self.vehiculo.modelo} | "
            f"Cédula: {self.chofer.documento} | "
            f"Chofer: {self.chofer.nombre}"
        )

# --- BASE DE DATOS (ARRAY) ---
base_de_datos_registros = []

# --- MENÚ ---
while True:
    print("\n--- MENÚ DE CONTROL DE ACCESO ---")
    print("1. Registrar nueva entrada")
    print("2. Ver todos los registros")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n[ Digitación de Datos ]")
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        doc = input("Cédula Chofer: ")
        nom = input("Nombre Chofer: ")
        
        # Crear objetos
        vehiculo = Vehiculo(placa, modelo)
        chofer = Chofer(doc, nom)
        registro = RegistroControl(vehiculo, chofer)
        
        # Guardar en el array
        base_de_datos_registros.append(registro)
        
        print("--------------------------------")
        print("Registro guardado correctamente")
        print("--------------------------------")
        
    elif opcion == "2":
        if not base_de_datos_registros:
            print("El arreglo está vacío. No hay datos digitados.")
        else:
            print("\n--------------------------------------------------------------")
            print("REPORTE DE DATOS GUARDADOS")
            print("--------------------------------------------------------------------------------------------------")
            for reg in base_de_datos_registros:
                print(reg.mostrar())
            print("--------------------------------------------------------------------------------------------------")

    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opción no válida, intente de nuevo.")
