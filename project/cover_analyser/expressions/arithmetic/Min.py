from Add import Add

class Min(Add):
    def __init__(self, var1, var2):
        super().__init__()
    def result(self):
        return self.var1 - self.var2