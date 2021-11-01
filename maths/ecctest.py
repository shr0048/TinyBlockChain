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

    def test_add(self):
        prime = 223
        a = FiniteField.FieldElement(0, prime)
        b = FiniteField.FieldElement(7, prime)

        add_points = [((170, 142), (60, 139)),
                      ((47, 71), (17, 56)),
                      ((143, 98), (76, 66))]

        add_res = [curve.Point(FiniteField.FieldElement(220, prime),
                               FiniteField.FieldElement(181, prime),
                               a, b),
                   curve.Point(FiniteField.FieldElement(215, prime),
                               FiniteField.FieldElement(68, prime),
                               a, b),
                   curve.Point(FiniteField.FieldElement(47, prime),
                               FiniteField.FieldElement(71, prime),
                               a, b)
                   ]

        points = []
        for coordinate_1, coordinate_2 in add_points:
            points.append(
                (
                    curve.Point(FiniteField.FieldElement(coordinate_1[0], prime),
                                FiniteField.FieldElement(coordinate_1[1], prime),
                                a, b
                                ),
                    curve.Point(FiniteField.FieldElement(coordinate_2[0], prime),
                                FiniteField.FieldElement(coordinate_2[1], prime),
                                a, b
                                )
                )
            )

        for idx, point in enumerate(points):
            self.assertEqual(point[0] + point[1], add_res[idx])
