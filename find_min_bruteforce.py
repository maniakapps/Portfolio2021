def find_min(a,b,c):
    if a < b and a < c:
        print(a)
    elif b < c and b < c:
        print(b)
    elif c < a and c < b:
        print(c)
    else:
        if a == b:
            print("a",a)
        if b == c:
            print("b",b)
        else:
            print(c)


find_min(4,2,2)