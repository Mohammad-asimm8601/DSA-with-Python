def clearTheIthBit(n, i):
    clear_bit = n & ~(1 << i)
    return bin(clear_bit)[2:]

n = 13
i = 2

result = clearTheIthBit(n, i)
print(result)