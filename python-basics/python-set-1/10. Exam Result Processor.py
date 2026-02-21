mark_list = list(map(int, input("Enter marks separated by space: ").split()))

total = sum(mark_list)
avg = total / len(mark_list)

# Check failure first
if any(mark < 35 for mark in mark_list):
    print("FAILED")

elif avg >= 75:
    print("DISTINCTION")

else:
    print("PASS")

