from xml.etree.cElementTree import Element,SubElement
from prettyfy import pretty

top = Element('autokomis')

#pierwszy samochód
sam1 = SubElement(top,'samochod')

id = SubElement(sam1,'id')
id.text = 'sam1'

marka = SubElement(sam1,'marka')
marka.text = 'Subaru'

model = SubElement(sam1,'model')
model.text = 'Impreza'

poj = SubElement(sam1,'pojemnosc')
poj.text = '2.0'

rocznik = SubElement(sam1,'rocznik')
rocznik.text = '1999'

cena = SubElement(sam1,'cena')
cena.text = '51000'

wyp_dod = SubElement(sam1,'wyposazenie_dod')

kolor = SubElement(wyp_dod,'kolor')
kolor.text = 'Czarna Perła'

SubElement(wyp_dod,'klimatyzacja').text = 'REE432432'

print(pretty(top))

with open("subaru.xml","a",encoding="UTF-8") as f:
    f.write(pretty(top))
