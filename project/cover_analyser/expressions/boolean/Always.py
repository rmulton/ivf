from .Bool import Bool

class Always(Bool):
    def __init__(self):
        super().__init__()

    def result(self):
        return True