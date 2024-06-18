class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
        
    def __str__(self):
        return f'Empleado: \n Nombre: {self.nombre}, Sueldo: {self.sueldo}'
    
    def mostrar_detalle(self):
        return self.__str__()