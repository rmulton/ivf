from cover_analyser.Var import Var

class Equal:
    """
    Représente l'opérateur booléean d'égalité
    .result() renvoie True si var1 et var2 ont la même valeur
    """
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
    def conditions(self):
        return [self]

class InfOrEqual:
    """
    Représente l'opérateur booléean d'inégalité
    .result() renvoie True si var1 a une valeur supérieure ou égale à celle de var2
    """
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
    def conditions(self):
        return [self]

class And:
    """
    Permet de composer deux booléens selon l'opérateur And
    """
    def __init__(self, bool1, bool2, no=False):
        super().__init__()
        self.bool1 = bool1
        self.bool2 = bool2
        self.no = no
    def result(self):
        if not self.no:
            return (self.bool1.result() and self.bool2.result())
        else:
            return not (self.bool1.result() and self.bool2.result())
    def variables(self):
        return self.bool1.variables() + self.bool2.variables()
    def conditions(self):
        return self.bool1.conditions() + self.bool2.conditions()

class Or:
    """
    Permet de composer deux opérateurs booléens selon l'opérateur or
    """
    def __init__(self, bool1, bool2, no=False):
        super().__init__()
        self.bool1 = bool1
        self.bool2 = bool2
        self.no = no

    def result(self):
        if not self.no:
            return (self.bool1.result() or self.bool2.result())
        else:
            return not (self.bool1.result() or self.bool2.result())
    def variables(self):
        return self.bool1.variables() + self.bool2.variables()
    def conditions(self):
        return self.bool1.conditions() + self.bool2.conditions()

class Always:
    """
    Opérateur renvoyant toujours True
    """
    def __init__(self):
        super().__init__()

    def result(self):
        return True
    
    def variables(self):
        return list()
    
    def conditions(self):
        return list()