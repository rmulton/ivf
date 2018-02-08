class Add:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    
    def result(self):
        return self.var1+self.var2

class Min(Add):
    def __init__(self, var1, var2):
        super().__init__(var1, var2)
    def result(self):
        return self.var1 - self.var2

class Mult:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    def result(self):
        return self.var1*self.var2