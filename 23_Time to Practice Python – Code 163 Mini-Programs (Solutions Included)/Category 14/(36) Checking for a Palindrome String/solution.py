word = input("Enter a Word: ").lower()

# reversing the word
rev_word = reversed(word)

# print(rev_word)
# print(list(rev_word))

if list(rev_word) == list(word):
    print("It is a palindrome word")
else:
    print("It is NOT a palindrome word")
