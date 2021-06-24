

def binary_search(arr, guess):
    minimum = 0
    large = len(arr) - 1
    find = round((large-minimum)//2)
    if find == guess:
        print("Great you guessed the number")
    elif find < guess:
        print("NUmber is greater")
    elif find > guess:
        print("NUmber is less")

arr = [1,2,3,4,5,6,7,8,9]
guess = 5
res = binary_search(arr, guess)
print(res)