from .Bool import Bool

class InfOrEqual(Bool):
    def __init__(self, var1, var2, no=None):
        super().__init__()
        self.var1 = var1
        self.var2 = var2
        self.no = no

    def result(self):
        if self.no == None or self.no == False:
            return self.var1 <= self.var2
        elif self.no == True:
            return self.var1 > self.var2

