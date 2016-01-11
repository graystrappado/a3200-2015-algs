from math import inf

insertion_max = 24


def insertion_sort(seq, start, end):
    for j in range(start + 1, end):
        key = seq[j]
        i = j - 1
        while i >= start and seq[i] > key:
            seq[i + 1] = seq[i]
            i -= 1
        seq[i + 1] = key
    return seq


def merge(seq, start, middle, end):
    i1 = middle - start
    i2 = end - middle
    left = []
    right = []

    for i in range(0, i1):
        left.append(seq[start + i])
    left.append(inf)
    for j in range(0, i2):
        right.append(seq[middle + j])
    right.append(inf)

    i = 0
    j = 0
    for k in range(start, end):
        if left[i] < right[j]:
            seq[k] = left[i]
            i += 1
        else:
            seq[k] = right[j]
            j += 1

    return seq


def merge_sort(seq, start, end):
    if end - start > insertion_max:
        middle = start + (end - start) // 2
        merge_sort(seq, start, middle)
        merge_sort(seq, middle, end)
        merge(seq, start, middle, end)
    else:
        insertion_sort(seq, start, end)
    return seq
