list1 = ["Hello ", "Hi "]
list2 = ["Dear", "Sir"]

result = [x + y for x in list1 for y in list2]
print(result)
