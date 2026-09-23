# Sum of 1 to n [parameterized]

def sumOf1ToN(sum, n):
    if n == 0:
        print(sum)
        return 
    sum += n
    sumOf1ToN(sum, n-1)

sumOf1ToN(0, 10)


# Functional recursion

def sumOf1ToN(n):
    if n == 1:
        return 1 
    return n + sumOf1ToN(n-1)

result = sumOf1ToN(10)
print(result)