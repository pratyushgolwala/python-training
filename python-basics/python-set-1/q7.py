bill = int(input())
if bill >=5000:
    print(bill - bill*0.2)
elif bill >=3000:
    print(bill - bill*0.1)
elif bill >=1000:
    print(bill - bill*0.05)
else:
    print(bill)
    