from random import randint


def random_array(low, high, size):
    seq = [0] * size
    i = 0
    while i < size:
        seq[i] = randint(low, high)
        i += 1
    return seq


def semi_sorted_array(low, high, size):

    seq = [0] * size

    value = randint(low, high)
    seq[0] = value

    sign = 1
    i = 1
    while i < size:
        if randint(0, 10) == 0:
            sign *= -1
        new_value = seq[i - 1] + sign * randint(0, 1 + high // 10)
        if new_value >= high or new_value < low:
            sign *= -1
            seq[i] = randint(low, high)
        else:
            seq[i] = new_value
        i += 1

    return seq


def ascending_sorted_array(low, high, size):
    seq = random_array(low, high, size)
    seq.sort()
    return seq


def descending_sorted_array(low, high, size):
    seq = ascending_sorted_array(low, high, size)
    seq.reverse()
    return seq


def same_value_array(low, high, size):
    num = randint(low, high)
    return [num] * size
