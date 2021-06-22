n = 1
nbr1 = 0
nbr2 = 1
if n == 0:
    print(n)
else:
    print(nbr1)
    print(nbr2)
    for i in range(1, n):
        nbr3 = nbr2 + nbr1
        print(nbr3)
        nbr1 = nbr2
        nbr2 = nbr3
