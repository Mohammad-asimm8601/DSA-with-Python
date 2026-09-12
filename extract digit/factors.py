# Method -1 brute force

def printFactors1(num):
    list = []
    for i in range(1, num+1):
        if num % i == 0:
            list.append(i)
    return list



factors = printFactors1(19)
print(factors)


# Method - 2   Average

def printFactors2(num):
    list = []
    for i in range(1, num//2):
        if num % i == 0:
            list.append(i)
    list.append(num)
    return list


factors = printFactors2(19)
print(factors)


# Method - 3    optimal
def printFactorial3(num):
    list = []
    
    for i in range(1, int(num **0.5)+1):
        if num % i == 0:
            list.append(i)
            if num // i != i:
                list.append(num//i)
    list.sort()
    return list

factors = printFactorial3(36)
print(factors)     