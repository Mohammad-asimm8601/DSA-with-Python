def binaryToDecimal(binary):
    num = 0
    pow = 0
    for i in range(len(binary)-1, -1, -1):
        num = num + int(binary[i])*(2**pow)
        pow += 1

    return num

binary_num = "1001"
result = binaryToDecimal(binary_num)
print(result)