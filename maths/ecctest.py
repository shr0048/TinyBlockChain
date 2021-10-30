from unittest import TestCase
import FiniteField
import curve


class ECCTest(TestCase):
    def test_is_on_curve(self):
        prime = 223
        a = FiniteField.FieldElement(0, prime)
        b = FiniteField.FieldElement(7, prime)
        valid_points = ((192, 105), (17, 56), (1, 193))
        invalid_points = ((200, 119), (42, 99))

        # Pass case
        for x, y in valid_points:
            x = FiniteField.FieldElement(x, prime)
            y = FiniteField.FieldElement(y, prime)
            curve.Point(x, y, a, b)

        # Fail case
        for x, y in invalid_points:
            x = FiniteField.FieldElement(x, prime)
            y = FiniteField.FieldElement(y, prime)

            with self.assertRaises(ValueError):
                curve.Point(x, y, a, b)
