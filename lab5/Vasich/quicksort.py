import random


def partition(seq, start, end):
    p = random.randint(start, end - 1)
    seq[p], seq[end - 1] = seq[end - 1], seq[p]
    pivot = seq[end - 1]

    lower_mid = j = start
    upper_mid = end - 1
    while j <= upper_mid:
        if seq[j] < pivot:
            seq[lower_mid], seq[j] = seq[j], seq[lower_mid]
            lower_mid += 1
            j += 1
        elif seq[j] > pivot:
            seq[upper_mid], seq[j] = seq[j], seq[upper_mid]
            upper_mid -= 1
        else:
            j += 1

    return lower_mid, upper_mid


def quicksort(seq, start, end):
    if start < end - 1:
        lower_mid, upper_mid = partition(seq, start, end)
        quicksort(seq, start, lower_mid)
        quicksort(seq, upper_mid + 1, end)
    return seq
