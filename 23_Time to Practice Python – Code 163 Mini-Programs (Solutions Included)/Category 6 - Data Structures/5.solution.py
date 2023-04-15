set1 = {65, 42, 78, 83, 23, 57, 29}
set2 = {67, 73, 43, 48, 83, 57, 29}


intersection = set1.intersection(set2)
print(intersection)

for item in intersection:
    set1.remove(item)

print(set1)
