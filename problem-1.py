class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.op = operation.strip().lower()

    def calculate(self):
        if self.op in ("addition", "add", "+"):
            return self.a + self.b
        elif self.op in ("subtraction", "subtract", "sub", "-"):
            return self.a - self.b
        elif self.op in ("multiplication", "multiply", "mul", "*"):
            return self.a * self.b
        elif self.op in ("division", "divide", "/"):
            if self.b == 0:
                return "Error: Division by zero not allowed."
            return self.a / self.b
        else:
            return "Invalid operation."

if __name__ == "__main__":
    a = input("Enter a (double): ").strip()
    b = input("Enter b (double): ").strip()
    op = input("Enter operation (Addition/Subtraction/Multiplication/Division or + - * /): ").strip()
    calc = Calculator(a, b, op)
    print("Result:", calc.calculate())
