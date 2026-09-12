
def check_palindrome(num):
    actual_num = num
    rev_num = 0
    while(num > 0):
        last_digit = num % 10
        rev_num = rev_num*10 + last_digit
        num = num//10
    
    if rev_num == actual_num:
        return "Palindrome"  
    else:
        return "Not a palindrome!"
    

result = check_palindrome(121)
print(result)