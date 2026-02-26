sequences = [
    "TATAGCGCGC",   # pass
    "TATAGGGCC",    # pass
    "TATACCGG",     # fail (exact 0.5)
    "GGGCCC",       # fail (no TATA)
    "TATAGCCCCC"    # pass
]
result = []

for i in sequences:
    if "TATA" in i and (i.count("G") + i.count("C"))/ len(i) > 0.5:
        result.append(i)

print(result)