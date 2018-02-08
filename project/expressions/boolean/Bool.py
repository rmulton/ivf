from ..arithmetic.Arithm import Arithm

class Bool():
    def __init__(self,value):
        self.value = value
        if not isinstance(self.value,bool)
            raise ValueError('Value must be True or False')
