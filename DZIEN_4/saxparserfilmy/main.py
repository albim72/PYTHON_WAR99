import xml.sax

class UchwytFilmu(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.id = ""
        self.tytul = ""
        self.rok = ""
        self.kraj = ""
        self.czas_t = ""
        self.gatunek = ""

    def startElement(self, tagname, attrs):
        self.current_data = tagname
        if tagname == "film":
            print("________________ film ____________________")

    def endElement(self, tagname):
        if self.current_data == "id_filmu":
            print(f'identyfikator filmu: {self.id}')
        elif self.current_data == "tytul":
            print(f'tytuł filmu: {self.tytul}')
        elif self.current_data == "rok":
            print(f'rok produkcji filmu: {self.rok}')
        elif self.current_data == "kraj":
            print(f'kraj produkcji filmu: {self.kraj}')
        elif self.current_data == "czas_trwania":
            print(f'czas trwania filmu: {self.czas_t}')
        elif self.current_data == "gatunek":
            print(f'gatunek filmu: {self.gatunek}')
            
    
        
    
        
    
