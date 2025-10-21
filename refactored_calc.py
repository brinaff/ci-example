class RefactoredCalculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("division by zero")
        return a / b

    def calculate(self, a, b, op):
        operations = {
            "add": self.add,
            "sub": self.sub,
            "mul": self.mul,
            "div": self.div
        }
        if op not in operations:
            raise ValueError("Invalid operation")
        return operations[op](a, b)
