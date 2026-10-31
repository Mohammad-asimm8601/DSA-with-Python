def toggleTheIthBit(n, i):
    toggle_bit = n ^ 1 << i
    return bin(toggle_bit)[2:]

n = 13
i = 1 
result = toggleTheIthBit(n, i)
print(result)