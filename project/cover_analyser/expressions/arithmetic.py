from cover_analyser.Var import Var

class Add:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    
    def result(self):
        if not isinstance(self.var1, Var):
            value1 = self.var1.result().value
        else:
            value1 = self.var1.value

        if not isinstance(self.var2, Var):
            value2 = self.var2.result().value
        else:
            value2 = self.var2.value
        res = value1 + value2
        return Var(value=res)
    def variables(self):
        variables = list()
        if isinstance(self.var1, Var):
            variables.append(self.var1)
        if isinstance(self.var2, Var):
            variables.append(self.var2)
        return variables


class Min(Add):
    def __init__(self, var1, var2):
        super().__init__(var1, var2)
    def result(self):
        if not isinstance(self.var1, Var):
            value1 = self.var1.result()
        else:
            value1 = self.var1.value
        if not isinstance(self.var2, Var):
            value2 = self.var2.result()
        else:
            value2 = self.var2.value
        res = value1 - value2
        return Var(value=res)
    def variables(self):
        variables = list()
        if isinstance(self.var1, Var):
            variables.append(self.var1)
        if isinstance(self.var2, Var):
            variables.append(self.var2)
        return variables

class Mult:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    def result(self):
        if not isinstance(self.var1, Var):
            value1 = self.var1.result()
        else:
            value1 = self.var1.value

        if not isinstance(self.var2, Var):
            value2 = self.var2.result()
        else:
            value2 = self.var2.value

        res = value1 * value2
        return Var(value=res)
    def variables(self):
        variables = list()
        if isinstance(self.var1, Var):
            variables.append(self.var1)
        if isinstance(self.var2, Var):
            variables.append(self.var2)
        return variables
