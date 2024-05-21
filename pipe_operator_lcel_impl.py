from types import UnionType
from typing import Any

class Runnable:

    def __init__(self , func):
        self.func = func

    def __or__(self, other):
        def _function(*args, **kargs):
            return other(self.func(*args, **kargs))
        return Runnable(_function)

    def __call__(self, *args, **kargs):
        return self.func(*args, **kargs)
        
if __name__ == '__main__': 

    def add_3(x):
        return x + 3
    
    def add_5(x):
        return x + 5
    
    add_3 = Runnable(add_3)
    chain = add_3 | add_5

    print(chain(4))