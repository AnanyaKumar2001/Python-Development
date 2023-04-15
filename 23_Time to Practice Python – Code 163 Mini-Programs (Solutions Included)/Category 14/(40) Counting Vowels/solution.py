string = input("Enter a Word/Sentence: ").lower()

vowels = "aeiou"

count = {}.fromkeys(vowels, 0)
print(count)

# counting vowels
for char in string:
    if char in count:
        count[char] += 1

print(count)
