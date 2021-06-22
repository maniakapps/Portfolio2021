"""
  AB pattern program
  starts with A in the first row then AB in the next few rows
"""
a = 'A'
b = 'B'


def triangle():
    n = int(input())
    for i in range(1, n+1):
        if i % 2 == 0:
            print((a + b) * int(i / 2))
        else:
            print((a + b) * int(i / 2) + a)


triangle()
