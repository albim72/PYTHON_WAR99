from funkcje.bfunkcje import czytaj_liste as cl, czytaj_slownik as cs

class CDane:
    def __init__(self,lista,slownik):
        self.lista=lista
        self.slownik=slownik
        
    def readl(self):
        return cl(self.lista)
    
    def readdict(self):
        return cs(self.slownik)
