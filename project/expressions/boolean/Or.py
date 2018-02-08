from .Bool import Bool

class Or(Bool):
    def __init__(self, bool1, bool2):
        super().__init__()
        self.bool1 = bool1
        self.bool2 = bool2

    def result(self):
        return (self.bool1 or self.bool2)

