def count_digit(num):
    if num == 0:
        return 1
    nod = 0
    while(num > 0):
        num = num // 10
        nod +=1
    return nod

def check_armstrong_num(num):
    actual_num = num
    nod = count_digit(num)
    total = 0

    while(num > 0):
        last_digit = num%10 
        total += last_digit**nod
        num = num // 10

    return total == actual_num

result = check_armstrong_num(153)
print(result)
