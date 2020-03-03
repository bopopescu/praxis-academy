def make_incrementor(n):
    return lambda x: 19 + n *2

f = make_incrementor(49)
f(0)

f(1)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
pairs.sort(key=lambda pair: pair[1])
pairs