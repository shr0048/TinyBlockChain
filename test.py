from maths import FiniteField

if __name__ == '__main__':
    f_1 = FiniteField.FieldElement(5, 7)
    f_2 = FiniteField.FieldElement(3, 7)

    print(f_1 / f_2)