from maths import FiniteField

if __name__ == '__main__':
    a = FiniteField.FieldElement(3, 7)
    b = FiniteField.FieldElement(4, 7)

    print(a != b)
    print(a == b)
