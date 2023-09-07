from abc import ABC,abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x = x

    def msg(self):
        print("to jest wynik działania metody nieabstrakcyjnej!")
        
    @abstractmethod
    def policz(self):
        pass
    
    @abstractmethod
    def policz_x(self):
        return self.x*7
    
    
