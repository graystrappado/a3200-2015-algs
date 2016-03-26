
def distance(a, b):
    m, n = len(a), len(b)

    if m < n:
        a, b = b, a
        m, n = n, m

    while n > 0 and a[m - 1] == b[n - 1]:
        m -= 1
        n -= 1
    start = 0
    while start < n and a[start] == b[start]:
        start += 1
    m -= start
    n -= start
    if n == 0:
        return m

    current_row = [j for j in range(n + 1)]
    old_row = [0 for _ in range(n + 1)]

    for i in range(1, m + 1):
        the_oldest_row, old_row, current_row = old_row, current_row, [i] + [0] * n
        for j in range(1, n + 1):
            i1, j1 = start + i - 1, start + j - 1
            cost = a[i1] != b[j1]
            delete, add, change = old_row[j] + 1, current_row[j - 1] + 1, old_row[j - 1] + cost
            if i > 1 and j > 1 \
                    and a[i1 - 1] == b[j1] \
                    and a[i1] == b[j1 - 1] and cost:
                swap = the_oldest_row[j - 2] + 1
                current_row[j] = min(add, delete, change, swap)
            else:
                current_row[j] = min(add, delete, change)

    return current_row[n]


#if __name__ == "__main__":
#    print(distance("abc", "cb"))

