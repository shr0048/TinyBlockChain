from maths import FiniteField
from elliptic_curve import curve

if __name__ == '__main__':
    f_1 = FiniteField.FieldElement(5, 7)
    f_2 = FiniteField.FieldElement(3, 7)

    print(f_1 / f_2)

    curve_1 = curve.Point(-1, -1, 5, 7)
    curve_2 = curve.Point(-1, -1, 5, 7)
    res = curve_1 + curve_2

    print(res.x, res.y)
