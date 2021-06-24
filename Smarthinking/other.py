def read_values():
    values =[]
    end='a'
    print("values")
    while end.upper() != 'Q':
        end = input()
        if end.upper() != 'Q':
            values.append(float(end))
    return values

def main():
    num = read_values()
    print(num)

main()