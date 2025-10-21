class OldCalculator:
    def calculate(self, a, b, op):
        if op == "add":
            return a + b
        elif op == "sub":
            return a - b
        elif op == "mul":
            return a * b
        elif op == "div":
            if b == 0:
                raise ValueError("division by zero")
            return a / b
        else:
            raise ValueError("Invalid operation")