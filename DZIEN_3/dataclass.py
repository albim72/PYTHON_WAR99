from dataclasses import dataclass,astuple,asdict,field

@dataclass
class Person:
    city:str
    firstname:str = "Jan"
    lastname:str = "Kot"
    age:int = 30
    job:str = "Data Developer"
    full_name:str = field(init=False,repr=False)
    
    # def __init__(self,firstname,lastname,age):
    #     self.firstname = firstname
    #     self.lastname = lastname
    #     self.age = age
        

    def __repr__(self):
        return f'Pracownik {self.firstname} {self.lastname}, stanowisko: {self.job}'
    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname

os1 = Person("Kraków")
print(os1)
print(os1.full_name)

print("_______________________________________________________")
os2 = Person("Kielce","Olga","Nowak",46,"Prezes")
print(os2)
print(os2.full_name)

print(astuple(os1))
print(astuple(os2))

print(asdict(os1))
print(asdict(os2))
