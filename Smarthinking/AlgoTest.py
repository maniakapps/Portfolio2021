import time

x = [1,2,3,4,5]
for i in range(len(x) + 1):
    if x[i] > x[i+1]:
        temp = x[i]
        x[i+1] = temp
        x[i] = temp

print(x)