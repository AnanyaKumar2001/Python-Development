def find_digits_chars_symbols(str):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in str:
        if char.islower() or char.isupper():
            char_count += 1
        elif char.isnumeric():
            digit_count += 1
        else:
            symbol_count += 1

    print(
        f"Character Count: {char_count}, Digit Count: {digit_count}, Symbol Count: {symbol_count}")


str = "h@#el26a^&5le"

find_digits_chars_symbols(str)
