// Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
 // Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
  // Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self) -> float:
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "sub":
            return self.a - self.b
        elif self.operation == "mul":
            return self.a * self.b
        elif self.operation == "div":
            if self.b != 0:
                return self.a / self.b
            else:
                raise ZeroDivisionError("Division by zero is not allowed.")
        else:
            raise ValueError("Invalid operation. Use add, sub, mul, or div.")


if __name__ == "__main__":
    try:
        a = float(input("Enter first number (a): "))
        b = float(input("Enter second number (b): "))
        op = input("Enter operation (add / sub / mul / div): ")

        calc = Calculator(a, b, op)
        result = calc.calculate()
        print(f"Result of {op} operation: {result}")
    except Exception as e:
        print(f"Error: {e}")
