code = []
for a in range (2, 21):
    a += 1
    for b in range (1, 21):
        for c in range (1, 21):
            a != b
            a != c
            if a % (b + c)==0:
                code.append(b)
                code.append(c)
                print( a, code)