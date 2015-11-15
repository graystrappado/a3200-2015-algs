radix = 10


def radix_sort(seq):
    p = 0
    done = False
    while done is False:
        done = True
        digits = [[] for _ in range(0, radix)]
        for i in range(0, len(seq)):
            div = (seq[i] // (radix ** p))
            if div != 0 and div != -1:
                done = False
            digits[div % radix].append(seq[i])
        j = 0
        for d in range(0, radix):
            digit = digits[d]
            for k in range(0, len(digit)):
                seq[j] = digit[k]
                j += 1
        p += 1

    signs = [[] for _ in range(0, 2)]
    for i in range(0, len(seq)):
        if seq[i] < 0:
            signs[0].append(seq[i])
        else:
            signs[1].append(seq[i])
    j = 0
    for s in range(0, 2):
        sign = signs[s]
        for k in range(0, len(sign)):
                seq[j] = sign[k]
                j += 1
    return seq
