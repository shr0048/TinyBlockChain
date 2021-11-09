class Point:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

        # That is infinite case, (identity of addition)
        if self.x is None and self.y is None:
            return
        if self.y ** 2 != self.x ** 3 + a * x + b:
            raise ValueError(f'{x}, {y} is not on the curve')

    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        else:
            return 'Point({},{})_{}'.format(self.x.num, self.y.num, self.x.prime)

    def __eq__(self, other):
        return self.x == other.x and \
               self.y == other.y and \
               self.a == other.a and \
               self.b == other.b

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            return TypeError(f'{self}, {other} are not same curve')

        # if either operator is the identity of addition
        if self.x is None and self.y is None:
            return other
        if other.x is None and other.y is None:
            return self

        # other is '-self'
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)

        # if add same point
        if self == other:
            # when 'y=0' then return identity of addition
            if self.y == 0 * self.x:
                return self.__class__(None, None, self.a, self.b)

            else:
                s = (3 * self.x ** 2 + self.a) / (2 * self.y)
                new_x = (s ** 2) - (2 * self.x)
                new_y = s * (self.x - new_x) - self.y
                return self.__class__(new_x, new_y, self.a, self.b)

        # Normal case
        s = (other.y - self.y) / (other.x - self.x)
        new_x = s ** 2 - self.x - other.x
        new_y = s * (self.x - new_x) - self.y

        return self.__class__(new_x, new_y, self.a, self.b)

    def __rmul__(self, coefficient):
        coef = coefficient
        current = self
        result = self.__class__(None, None, self.a, self.b)

        while coef:
            if coef & 1:
                result += current
            current += current
            coef >>= 1

        return result
