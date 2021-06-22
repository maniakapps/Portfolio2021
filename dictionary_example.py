"""
    Tables lookup
"""
lista = [['google','hello'],['yahoo','hola']]
selected = input()
r, col = 0, 1
"""for row in lista:
    if row[0] == selected:
        print(lista[r][col])
    else:
        r+=1"""
ishere = False
for keyvalue in lista:
    website=keyvalue[0]
    if selected == website:
        print("\n" + website)
        ishere = True
    encrypted = keyvalue[1]

if not ishere:
    print("SIte wasn't found")