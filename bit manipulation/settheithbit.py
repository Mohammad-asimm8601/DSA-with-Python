def setTheIthBit(n, i):
    set_bit = n | (1 <<i)
    return bin(set_bit)[2:]

n = 9
i = 2
result = setTheIthBit(n, i)
print(result)