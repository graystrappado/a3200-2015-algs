def one_pass_sum(seq, indices):
    max_sum = float("-inf")
    curr_sum = 0
    height = seq[indices[0]]

    for i in indices[1:]:
        if seq[i] < height:
            curr_sum += height - seq[i]
        else:
            if curr_sum >= max_sum:
                max_sum = curr_sum
            height = seq[i]
            curr_sum = 0
    return max_sum


def chart_area(seq):
    if len(seq) < 3:
        return 0

    forward = one_pass_sum(seq, range(len(seq)))
    backward = one_pass_sum(seq, range(len(seq) - 1, -1, -1))

    return max(forward, backward)
