class Assign:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    def run(self):
        self.var1.value = self.var2.value