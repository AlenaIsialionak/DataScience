def check(your: tuple, enemy: tuple) -> bool:
    steps = [(-1, 2), (1, 2), (-1, -2), (1, -2)]

    x1, y1 = your
    x2, y2 = enemy

    for step in steps:
        a, b = step
        if 0 <= x1 + a <= 8 and x1 + a == x2 and 0 <= y1 + b <= 8 and y1 + b == y2:
            return True
    return False


# print(check((6, 6), (7, 5)))


def different_array(size_array: int):
    result = []

    str1 = [['0'] * size_array for _ in range(size_array)]
    print(str1)

    for i in range(size_array):

        for j in range(size_array):
            if i < size_array//2 + 1:
                if j >= size_array - i - 1:
                    str1[i][j] = "1"
            else:
                if j > i - 1:
                    str1[i][j] = "1"
    for s in str1:
        print(s)

different_array(5)





