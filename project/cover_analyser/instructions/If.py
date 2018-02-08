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