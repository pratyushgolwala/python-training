change = int(input("Enter the change:"))
atm = [1000, 500, 100, 50, 10, 5, 2, 1]
opt = []
note_num = 0
freq = {}

for i in atm:
    while change >= i:
        change -= i
        opt.append(i)
        note_num += 1
for num in opt:
    freq[num] = freq.get(num, 0) + 1
print(f"num of notes = {note_num} ")
print(f"number of notes = {freq} ")
