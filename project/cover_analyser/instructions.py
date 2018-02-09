from cover_analyser.Var import Var

class Assign:
    """
    Représente une instruction d'assignation de la valeur contenue par var2 à la valeur contenue par var1.
    """
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    def run(self):
        if not isinstance(self.var2, Var):
            value2 = self.var2.result().value
        else:
            value2 = self.var2.value
        self.var1.value = value2
    def variables(self):
        variables = list()
        if isinstance(self.var1, Var):
            variables.append(self.var1)
        if isinstance(self.var2, Var):
            variables.append(self.var2)
        return variables

class If:
    """
    Représente une boucle If. instruction_if est executée si la condition est
    vraie, sinon on exécute instruction_else
    """
    def __init__(self, condition, instruction_if, instruction_else):
        self.condition = condition
        self.instruction_if = instruction_if
        self.instruction_else = instruction_else

    def run(self):
        if self.condition.result():
            self.instruction_if.run()
        else :
            self.instruction_else.run()
    
    def variables(self):
        return self.condition.variables() + self.instruction_if.variables() + self.instruction_else.variables()

class Skip:
    """
    Représente une instruction Skip
    """
    def __init__(self):
        return

    def run(self):
        pass

    def variables(self):
        return list()