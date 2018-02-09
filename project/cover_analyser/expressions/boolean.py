from cover_analyser.Var import Var
class And:
    def __init__(self, bool1, bool2):
        super().__init__()
        self.bool1 = bool1
        self.bool2 = bool2
    def result(self):
        return (self.bool1.result() and self.bool2.result())
    def variables(self):
        return self.bool1.variables() + self.bool2.variables()

class Equal:
    def __init__(self,var1,var2, no = False):
        super().__init__()
        self.var1 = var1
        self.var2 = var2
        self.no = no
    def result(self):
        if not isinstance(self.var1, Var):
            value1 = self.var1.result()
        else:
            value1 = self.var1.value

        if not isinstance(self.var2, Var):
            value2 = self.var2.result()
        else:
            value2 = self.var2.value
        if self.no:
            return value1!=value2
        else:
            return value1==value2
    def variables(self):
        variables = list()
        if isinstance(self.var1, Var):
            variables.append(self.var1)
        if isinstance(self.var2, Var):
            variables.append(self.var2)
        return variables

class InfOrEqual:
    def __init__(self, var1, var2, no=False):
        super().__init__()
        self.var1 = var1
        self.var2 = var2
        self.no = no

    def result(self):
        if not isinstance(self.var1, Var):
            value1 = self.var1.result()
        else:
            value1 = self.var1.value

        if not isinstance(self.var2, Var):
            value2 = self.var2.result()
        else:
            value2 = self.var2.value

        if self.no:
            return value1 > value2
        else:
            return value1 <= value2
    def variables(self):
        variables = list()
        if isinstance(self.var1, Var):
            variables.append(self.var1)
        if isinstance(self.var2, Var):
            variables.append(self.var2)
        return variables

class Or:
    def __init__(self, bool1, bool2):
        super().__init__()
        self.bool1 = bool1
        self.bool2 = bool2

    def result(self):
        return (self.bool1.result() or self.bool2.result())
    def variables(self):
        return self.bool1.variables() + self.bool2.variables()

class Always:
    def __init__(self):
        super().__init__()

    def result(self):
        return True
    
    def variables(self):
        return list()