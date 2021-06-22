
ls = ['one','two','three','one']
d1 = {}
for x in ls:
    if x in d1:
        d1[x] += 1
    else:
        d1[x] = 1


print(d1)