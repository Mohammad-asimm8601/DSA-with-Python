def checkIthBitSetOrNot(n, i):
    if (n & (1 << i)) != 0:
        return True
    return False

n = 13
i = 2
result = checkIthBitSetOrNot(n, i)
print(result)