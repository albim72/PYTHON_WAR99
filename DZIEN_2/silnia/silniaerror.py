class SilniaError(Exception):
    def __init__(self,n):
        self.n=n
        
    def __str__(self):
        return (f'[{self.__class__.__name__}] n nie może wynosić: {self.n}, silnia nie jest '
                f'zdefiniowana dla liczb ujemnych')
