from sys import stdin, stdout


def triples(seq):
    # n log(n)
    seq.sort()

    arr = [seq[0] ** 2]

    j = 0

    # n
    for i in range(1, len(seq)):
        value = seq[i] ** 2
        if arr[j] != value:
            arr.append(value)
            j += 1

    if len(arr) < 3:
        return 0

    count = 0
    # n^2 (3SUM)
    for i in range(2, len(arr)):
        start = 0
        end = i - 1
        while start < end:
            if arr[start] + arr[end] == arr[i]:
                count += 1
                start += 1
                end -= 1
            elif arr[start] + arr[end] > arr[i]:
                end -= 1
            else:
                start += 1

    return count
