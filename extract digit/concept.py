# Concept of extract of digit using loop


# concept-1

num  = 2867
while(num > 0):
    last_digit = num % 10
    print(last_digit)
    num = int(num / 10)
