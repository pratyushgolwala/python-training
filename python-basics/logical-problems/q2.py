import random
N = int(input("Enter distinct coupon number: "))

count = 0
coupon_list = []
distinct_coupons = set()

while len(distinct_coupons) < N:
    coupon = random.randint(1,N)
    coupon_list.append(coupon)
    distinct_coupons.add(coupon)
    count += 1
print(f"Distinct coupons: {distinct_coupons}")
print(f"coupons list: {coupon_list}")
print(f"Total random numbers needed to get {N} distinct coupons: {count}")