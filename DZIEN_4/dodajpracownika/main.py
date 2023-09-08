import json

def dodaj_nowego_pracownika(new_data,filename="pracownik.json"):
    with open(filename,"r+",encoding="utf-8") as file:
        file_data = json.load(file)
        file_data["pra_info"].append(new_data)
        print(len(file_data["pra_info"]))
        file.seek(0)
        json.dump(file_data,file,indent=4)

nowyprac =  {
            "imie": "Daniel",
            "nazwisko": "Knotowski",
            "stanowisko": "koordynator",
            "lata_pracy": 1,
            "email": "dani@firma.pl"
        }

dodaj_nowego_pracownika(nowyprac)

