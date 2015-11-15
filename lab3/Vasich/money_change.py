from sys import stdin

_cash = int(stdin.readline())
second_line = stdin.readline()
coins = [int(c) for c in second_line.split(' ')]


def way_count(cash, coin_index):
    if cash == 0:
        return 1
    elif cash < 0 or coin_index == 0:
        return 0
    return way_count(cash - coins[coin_index - 1], coin_index) + way_count(cash, coin_index - 1)


print(way_count(_cash, len(coins)))
