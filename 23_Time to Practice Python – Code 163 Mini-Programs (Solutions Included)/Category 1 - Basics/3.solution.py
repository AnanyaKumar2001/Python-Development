def print_even_index(str):

    for char in range(0, len(str), 2):
        print("Index[", char, "]", str[char])


string = "learning"
print_even_index(string)
