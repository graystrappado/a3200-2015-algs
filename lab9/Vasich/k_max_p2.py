from sys import stdin, stdout


def find_pivot(seq, start, end, sub_length):
    medians = []
    sub_seq = []
    while end - start > sub_length:
        for i in range(start, start + sub_length):
            sub_seq.append(seq[i])
        sub_seq.sort()
        medians.append(sub_seq[2])
        start += sub_length
        sub_seq = []

    for i in range(start, end):
        sub_seq.append(seq[i])
    sub_seq.sort()
    medians.append(sub_seq[len(sub_seq) // 2])

    medians.sort()
    return medians[len(medians) // 2]


def partition(seq, start, end):
    pivot = find_pivot(seq, start, end, 5)

    lower_mid = j = start
    upper_mid = end - 1
    while j <= upper_mid:
        if seq[j] > pivot:
            seq[lower_mid], seq[j] = seq[j], seq[lower_mid]
            lower_mid += 1
            j += 1
        elif seq[j] < pivot:
            seq[upper_mid], seq[j] = seq[j], seq[upper_mid]
            upper_mid -= 1
        else:
            j += 1

    return lower_mid, upper_mid


def quickselect(seq, start, end, k):
    if start < end - 1:
        lower_mid, upper_mid = partition(seq, start, end)
        if k < lower_mid:
            return quickselect(seq, start, lower_mid, k)
        if k >= upper_mid:
            return quickselect(seq, upper_mid + 1, end, k)
    return seq[0:min(k, len(seq))]


