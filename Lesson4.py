def different_array1(size_array: int):
    str1 = [[0 for _ in range(size_array)] for _ in range(size_array)]

    for i in range(size_array):
        for j in range(size_array):
            if i < size_array//2 + 1:
                if j >= size_array - i - 1:
                    str1[i][j] = 1
            else:
                if j > i - 1:
                    str1[i][j] = 1
    for s in str1:
        print(s)


different_array1(5)


def different_array2(size_array: int):
    str1 = [[0] * size_array for _ in range(size_array)]

    for i in range(size_array):

        for j in range(size_array):
            if i < size_array//2 + 1:
                if j <= i or j >= size_array - i - 1:
                    str1[i][j] = 1
            else:
                if j < size_array - i or j > i - 1:
                    str1[i][j] = 1
    for s in str1:
        print(s)


print("***************")
different_array2(5)


def different_array3(size_array: int):

    str1 = [[0] * size_array for _ in range(size_array)]

    for i in range(size_array):
        for j in range(size_array//2 + 1):
            if i < size_array//2 + 1:
                if j >= i:
                    str1[i][j] = 1
                    str1[i][-j-1] = 1
            else:
                if j >= size_array - i - 1:
                    str1[i][j] = 1
                    str1[i][-j - 1] = 1
    for s in str1:
        print(s)


print("****************")
different_array3(5)



