class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = f"Num {num} not in field range 0 to {prime -1}"
            raise ValueError(error)

        self.num = num
        self.prime = prime

    def __repr__(self):
        return f"FiledElement_{self.prime}({self.num})"

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        return not(self == other)

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError("Can't add two numbers in different fields")

        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError("Can't sub two numbers in different fields")

        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError("Can't mul two numbers in different fields")

        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError("Can't div two numbers in different fields")
        return self * (other**(other.prime - 2))
