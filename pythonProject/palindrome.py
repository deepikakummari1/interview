n = 2112
original_n = n
reversed_n = 0
while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10
if original_n == reversed_n:
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")



s="madam"
rev=s[::-1]
if s==rev:
    print("the given string is palindrome")
else:
    print("the given string is not palindrome")
    

