# Using Recursion
def print1ton( i, num):
    if i > num:
        return
    print(i)
    print1ton(i+1, num)

print1ton(1, 5)

print()


# tail BackTracking
def print1ton(num):
    if num == 0:
        return
    print1ton(num - 1)
    print(num)

print1ton(5)