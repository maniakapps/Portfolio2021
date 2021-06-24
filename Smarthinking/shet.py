ONE_TEN = [1,2,3,4,5,6,7,8,9,10]

def main():
    print("hello")
    data = [ONE_TEN]
    data[0][1] = 345
    for i in range(1, len(data[0])-1):
        left = data[0][i - 1]
        right = data[0][i + 1]
        if left > right:
            data[0][i]= left
        else:
            data[0][i] = right
    print(data[0])


main()