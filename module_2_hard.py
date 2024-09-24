import random
def code (n, *key):
    code_n = []
    n = (3, 20)
    key = (1, 20)
    for n1 in range (random. choice(n)):
        n1 += 1
        code_n.append( n1)
        for key1 in (random. choice(key)):
            if n1 % key1 == 0:
                code_n[n1].append(key1)
    print(code_n)
