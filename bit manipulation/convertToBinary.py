def convert2Binary(num):
    binary = ""
    while num != 0:
        rem = num % 2
        binary += str(rem)
        num = num//2

    binary = binary[::-1]

    return binary

num = 18
result = convert2Binary(num)
print(result)