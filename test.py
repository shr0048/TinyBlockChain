from maths import FiniteField, curve

if __name__ == '__main__':
    prime = 223
    a = FiniteField.FieldElement(0, prime)
    b = FiniteField.FieldElement(7, prime)

    add_points = [((170, 142), (60, 139)),
                  ((47, 71), (17, 56)),
                  ((143, 98), (76, 66))]

    points = []
    for coordinate_1, coordinate_2 in add_points:
        try:
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

        except ValueError:
            print("Error")
            continue

    for point_1, point_2 in points:
        res = point_1 + point_2
        print(point_1.a, point_1.b, point_1.x, point_1.y)
        print(point_2.a, point_2.b, point_2.x, point_2.y)
        print(f"Add: {res.a, res.b, res.x, res.y}")
        print("\n")

