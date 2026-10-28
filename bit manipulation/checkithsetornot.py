def checkIthBitSetOrNot(n, i):
    result = ""
    while n != 0:
        result += str(n%2)
        n = n//2
    result = result[::-1]
    result = result 
    return result

n = 13
i = 1
result = checkIthBitSetOrNot(n, i)
print(result)