def palindrome(n):
    a = str(n)
    if a == a[::-1]:
       return 'PALINDROME'
    else:
        return 'NOT PALINDROME'
    

num = int(input())
print(palindrome(num))