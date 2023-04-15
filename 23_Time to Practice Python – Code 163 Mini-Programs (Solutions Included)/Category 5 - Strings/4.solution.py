str = "Lemon Malt"
str = "kiwi"

count_dict = dict()

for char in str:
    count = str.count(char)

    count_dict[char] = count

print(count_dict)
