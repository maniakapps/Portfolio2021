lst = [
    ['google', 'monsters'],
    ['yahoo', 'hello'],
    ['nubia', "marica"]
]
site = input("Enter a site: ")
index = -1
for i in lst:
    index += 1
    if site in i[0]:
        print("user: ", site)
        print("password: ", lst[index][1])
        break
else:
    print("not found")
