class Informe:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    def generar_informe(self):
        return f"Título: {self.titulo}\nContenido: {self.contenido}"

class GuardarInforme:
    @staticmethod
    def guardar_en_archivo(informe, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(informe.generar_informe())

informe = Informe("Mi Informe", "Este es el contenido.")
GuardarInforme.guardar_en_archivo(informe, "informe.txt")
