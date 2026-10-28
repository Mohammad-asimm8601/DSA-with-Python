def swapToNumber(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a,b

a = 8
b = 7
x,y = swapToNumber(a, b)
print(x, y)