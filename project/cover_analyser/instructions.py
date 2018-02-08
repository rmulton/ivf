class Assign:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def run(self):
        self.var1.value = self.var2.value


class If:
    def __init__(self, condition, instruction_if, instruction_else):
        self.condition = condition
        self.instruction_if = instruction_if
        self.instruction_else = instruction_else

    def run(self):
        if self.condition.result():
            self.instruction_if.run()
        else :
            self.instruction_else.run()


class Skip:
    def __init__(self):
        return

    def run(self):
        pass


class While:
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

    def run(self):
        while self.condition.result():
            self.instruction.run()