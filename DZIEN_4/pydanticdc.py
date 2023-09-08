import dataclasses
from typing import List,Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

@dataclass
class User:
    id:int
    name:str="Jan Kowalski"
    friends: List[str] = dataclasses.field(default_factory=lambda : ["brak"])
    age: Optional[int] = dataclasses.field(default=None,
                                           metadata=dict(title='Wiek użytkownika', description="nie kłam!"))
    height: Optional[float] = Field(None,title="wzrost w cm", ge=50,le=300)

user = User(id='33')
print(user)

usr2 = User(56,"Olga Kot",["Jula","Tomek"],56,173.5)
print(usr2)

k1 = (5)
k2 = (7,)

print(type(k1))
print(type(k2))
