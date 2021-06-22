def max_min(lst):
    final = []
    for x in lst:
        final.append(max(lst))
        final.append(min(lst))
        del lst[lst.index(min(lst))]
        del lst[lst.index(max(lst))]
    if len(lst) == 1:
        final.append(lst[0])
    return final


lst = [1,2,3,4,5]
print(max_min(lst))
