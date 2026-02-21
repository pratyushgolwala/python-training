binary = (input())
digit = 0
rev_binary = binary[::-1]
for i in range(0,len(binary)):
    if rev_binary[i] == '1':
        digit += 2**i
        i+=1
    else:
        digit+=0
        i+=1
print(digit)
    
    
