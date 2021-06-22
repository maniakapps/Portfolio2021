#exercise 5
print("Excersice 5")
print("===============")
phrases = ['Buckle my shoe', "shut the door", "pick up sticks", "Lay them straight","Your big fat hen"]
cnt = 0
for i in range(1, 11):
    print(i, end=' ')
    if i % 2 == 0:
        print(phrases[cnt])
        cnt += 1