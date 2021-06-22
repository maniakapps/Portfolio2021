"""
    Decimal to binary converter using a remainder approach
"""
a = 2

#print(bin(a).replace('0b',''))
result = ''
if a == 0:
    print(0)
else:
    while a > 0:
        remainder = a % 2  # gives the exact remainder
        a = a // 2
        result += str(remainder)

print(result[::-1])
