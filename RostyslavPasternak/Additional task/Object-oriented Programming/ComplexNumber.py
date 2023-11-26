import math

class ComplexNumber:
    """A class representing a complex number with real and imaginary parts.

    Attributes:
        real (float): The real part of the complex number.
        imag (float): The imaginary part of the complex number.
    """

    def __init__(self, real: float, imag: float):
        """Initialize a ComplexNumber object with the given real and imaginary parts.

        Parameters:
            real (float): The real part of the complex number.
            imag (float): The imaginary part of the complex number.
        """
        self.real = real
        self.imag = imag

    def conjugate(self):
        """Return the conjugate of the complex number."""
        return ComplexNumber(self.real, -self.imag)

    def __str__(self):
        """Return a string representation of the complex number."""
        if self.imag > 0:
            sign = "+"
        elif self.imag < 0:
            sign = "-"
        else:
            return str(self.real)


        return "(" + str(self.real) + sign + str(abs(self.imag)) + "j)"

    def __abs__(self):
        """Return the absolute value of the complex number."""
        return math.sqrt(pow(self.real, 2) + pow(self.imag, 2))

    def __eq__(self, other):
        """Check if two ComplexNumber objects are equal."""
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imag == other.imag
        elif isinstance(other, complex):
            return self.real == other.real and self.imag == other.imag
        return False

    def __add__(self, other):
        """Add two complex numbers."""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        raise ValueError("Unsupported operand type for +")

    def __sub__(self, other):
        """Subtract two complex numbers."""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        raise ValueError("Unsupported operand type for -")

    def __mul__(self, other):
        """Multiply two complex numbers."""
        if isinstance(other, ComplexNumber):
            return ComplexNumber((self.real * other.real) - (self.imag * other.imag),
                                 (self.real * other.imag) + (self.imag * other.real))
        raise ValueError("Unsupported operand type for *")

    def __truediv__(self, other):
        """Divide two complex numbers."""
        if isinstance(other, ComplexNumber):
            denominator = (pow(other.real, 2) + pow(other.imag, 2))
            return ComplexNumber((self.real * other.real + self.imag * other.imag) / denominator,
                                 (self.imag * other.real - self.real * other.imag) / denominator)
        raise ValueError("Unsupported operand type for /")
