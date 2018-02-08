class While:
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction
    def run(self):
        while self.condition.result():
            self.instruction.run()