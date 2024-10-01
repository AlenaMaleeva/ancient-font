n = input('Введите первое число шифра от 3 до 20: ')
n1 = int (n)
for b in range (1, 20):
    for c in range (1, 20):
        if b != c:
            if n1 % (b + c) == 0:
                result = b, c
                print(result, end=' ')



