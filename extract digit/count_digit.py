# count digit


# method -1

def count_digit(num):
    if num == 0:
        return 1
    count = 0
    num = abs(num)
    while(num > 0):
        count += 1
        num = int(num/10)
    return count

result = count_digit(0)
print(result)


# method-2

from math import log10

def count_digit(num):
    num  = abs(num)
    if num == 0: 
        return 1
    return int(log10(num) + 1)

result = count_digit(-1)
print(result)