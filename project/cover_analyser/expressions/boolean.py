class Bool():
    def __init__(self,value):
        self.value = value
        if not isinstance(self.value,bool)
            raise ValueError('Value must be True or False')

class And(Bool):
    def __init__(self, bool1, bool2):
        super().__init__()
        self.bool1 = bool1
        self.bool2 = bool2

    def result(self):
        return (self.bool1 and self.bool2)

class Equal(Bool):

    def __init__(self,var1,var2, no = None):
        super().__init__()
        self.var1 = var1
        self.var2 = var2
        self.no = no

    def result(self):
        if self.no == None or self.no == False:
            return self.var1 == self.var2
        elif self.no == True:
            return self.var1 != self.var2

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

class Or(Bool):
    def __init__(self, bool1, bool2):
        super().__init__()
        self.bool1 = bool1
        self.bool2 = bool2

    def result(self):
        return (self.bool1 or self.bool2)

class Always(Bool):
    def __init__(self):
        super().__init__()

    def result(self):
        return True