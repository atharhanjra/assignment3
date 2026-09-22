class Operations:
    """Groups the four basic arithmetic operations as static methods."""

    @staticmethod
    def addition(a: float, b: float) -> float:
        """Return the sum of a and b."""
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """Return a minus b."""
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """Return the product of a and b."""
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        """Return a divided by b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b