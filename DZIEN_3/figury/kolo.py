#utwórz klasę Kolo dziedziczącą Figurę
#wzrór na pole koła > pi*r**2
#wartość pi pobierz z pakietu math -> math.pi
#w pliku main.py policz pole koła dla wartości promienia = 5.5

from figura import Figura
import math

class Kolo(Figura):
    def __init__(self,a,b=math.pi):
        super().__init__(a,b)

    def policz_pole(self):
        return self.b*self.a**2

