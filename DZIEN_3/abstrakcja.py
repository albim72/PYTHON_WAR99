from abc import ABC,abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x = x

    def msg(self):
        return "to jest wynik działania metody nieabstrakcyjnej!"

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        e = self.x*7
        return e*1.2


class Regular(Prototyp):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y

    def policz(self):
        return self.y - 0.06*self.x

    def policz_x(self):
        return super().policz_x() + 21*self.y

    def msg(self):
        return super().msg() + "... ciąg dalszy"


rg = Regular(4,8)

print(rg.msg())
print(f'funkcja policz: {rg.policz()}')
print(f'funkcja policz_x: {rg.policz_x()}')
