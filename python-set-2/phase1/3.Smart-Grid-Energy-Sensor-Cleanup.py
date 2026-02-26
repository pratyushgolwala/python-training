readings = [[22, None, 25], [None, None, 19], [20, 21, 22]]
result = []
for lst in readings:
    lst = list(filter(lambda x :x != None, lst))
    avg = sum(lst) / len(lst)
    result.append(avg)
print(result)