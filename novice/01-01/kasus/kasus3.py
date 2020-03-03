a, b = 1, 2
print('angka dari A :')
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
    