import json

jsource = '{"imie":"Jan","nazwisko":"Nowak","wiek":40,"miasto":"Lublin"}'
print(jsource)
print(type(jsource))

osoba = json.loads(jsource)
print(osoba)
print(type(osoba))
print(osoba["nazwisko"])

auto = {
    "marka":"Jeep",
    "model":"Cherokee",
    "rocznik":2020,
    "poj":4.8
}

print(auto)
jsonauto = json.dumps(auto,indent=4)
print(jsonauto)

with open("autoj.json","w",encoding="utf-8") as f:
    f.write(jsonauto)

