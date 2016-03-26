import time


def palindrome(s):
    length = len(s)

    matrix = [[i == j for i in range(length)] for j in range(length)]

    for diagonal in range(1, length):
        for i, j in zip(range(length - 1), range(diagonal, length)):
            if s[i] == s[j]:
                matrix[i][j] = matrix[i + 1][j - 1] + 2
            else:
                matrix[i][j] = max(matrix[i][j - 1], matrix[i + 1][j])

    str_left, pal_left = 0, 0
    str_right, pal_right = length - 1, matrix[0][-1] - 1
    p = [""] * matrix[0][-1]

    while str_left <= str_right:
        if str_left == str_right:
            p[pal_left] = s[str_left]
            break
        if s[str_left] == s[str_right]:
            p[pal_left] = s[str_left]
            p[pal_right] = s[str_right]
            str_left += 1
            str_right -= 1
            pal_left += 1
            pal_right -= 1
        else:
            move = matrix[str_left + 1][str_right] > matrix[str_left][str_right - 1]
            str_left += move
            str_right += move - 1

    return "".join(p)


if __name__ == "__main__":
    pass
