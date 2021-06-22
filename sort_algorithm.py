from random import seed
from random import randint

seed(1)
ml = []


def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    r = (low - 1)
    d = high - 1
    while True:
        r += 1
        while arr[d] < pivot:
            r += 1
            d -= 1
        while arr[d] > pivot:
            d -= 1
        if r > d:
            return d


def quicksort(arr, low, high):
    if low < high:
        split_index = partition(arr, low, high)
        quicksort(arr, low, split_index - 1)
        quicksort(arr, split_index + 1, high)


for i in range(1000):
    value = randint(0, 1001)
    ml.append(value)

n = len(ml)
quicksort(ml, 0, n - 1)
for j in range(n):
    print("%d" % ml[j])
