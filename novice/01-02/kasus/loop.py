def nilai(n):   
    result = []
    a, b = 0, 1
    print('jumlah nilai :')
    while a < n:
        result.append(a)
        a, b = b, a+b * 2
    return result