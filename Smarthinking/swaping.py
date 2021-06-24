#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


swap = 0
for i in range(0, len(a) - 1):
    for i in range(0, n-i-1):
        right = a[i+1]
        if a[i] > right:
            a[i], a[i+1]  = a[i+1], a[i]
            swap += 1

print("Array is sorted in {0} swaps.".format(swap))
print("First element: ", a[0])
print("Last element: ", a[len(a)-1])
