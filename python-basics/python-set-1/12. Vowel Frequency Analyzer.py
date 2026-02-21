sentence = input()
count = 0
for i in sentence.split():
    for j in i:
        if j in "AEIOUaeiou":
            count+=1
print(count)