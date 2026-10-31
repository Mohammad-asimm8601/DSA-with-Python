def clearTheIthBit(n):
    result = n & n-1
    return bin(result)[2:]

n = 40

result = clearTheIthBit(n)
print(result)