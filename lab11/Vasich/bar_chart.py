
def chart_area(seq):
    if len(seq) < 3:
        return 0

    max_sum = float("-inf")

    height = seq[0]
    curr_sum = 0

    for i in range(1, len(seq)):
        if seq[i] < height:
            curr_sum += height - seq[i]
        else:
            if curr_sum >= max_sum:
                max_sum = curr_sum
            height = seq[i]
            curr_sum = 0

    height = seq[len(seq) - 1]
    curr_sum = 0

    for i in range(len(seq) - 2, -1, -1):
        if seq[i] < height:
            curr_sum += height - seq[i]
        else:
            if curr_sum >= max_sum:
                max_sum = curr_sum
            height = seq[i]
            curr_sum = 0

    return max_sum

