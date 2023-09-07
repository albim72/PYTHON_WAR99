from pojazd import Pojazd

p1 = Pojazd()
odl = 567
jed = 51
cj = 6.49

print(f'spalanie [l/100km]: {p1.spalanie(odl,jed):.2f}')
print(f'koszt przejzdu na odcinku {odl} km wynosi {p1.kosztyprzejazdu(odl,jed,cj):.2f} zł')
