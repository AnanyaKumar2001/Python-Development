first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print("First set is a subset of the second set", first_set.issubset(second_set))
print("Second set is a subset of the first set", second_set.issubset(first_set))


print("First set is a super set of the second set",
      first_set.issuperset(second_set))
print("Second set is a super set of the first set",
      second_set.issuperset(first_set))


if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()


print(first_set)
print(second_set)
