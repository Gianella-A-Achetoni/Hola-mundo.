
class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    #get and setter ancho
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho
        
    #get and setter alto
    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        self._alto = alto
        
    def __str__(self):
        return f'Figura Geometrica [Alto: {self._alto} y ancho: {self._ancho} ]'