# Using loop
def checkPalindrome(s):
    left = 0
    right = len(s)-1
    while(left < right):
        if(s[left] != s[right]):
            return "Not a Palindrome"
        left += 1
        right -= 1
    return "palindrome"
    

s = "madam"
result = checkPalindrome(s)
print(result)



# Using recursion

def palindrome(s, left, right):
    if left >= right:
        return "Palindrome"
    if s[left] != s[right]:
        return "Not a Palindrome"
    return palindrome(s, left+1, right-1)

result = palindrome(s, 0, len(s)-1)
print(result)