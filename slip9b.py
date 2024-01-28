

#Write a python program to count repeated characters in a string.
#Sample string: 'thequickbrownfoxjumpsoverthelazydog'
#Expected output: o-4, e-3, u-2, h-2, r-2, t-2


def count_repeated_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    repeated_chars = {char: count for char, count in char_count.items() if count > 1}

    repeated_chars_formatted = ", ".join([f"{char}-{count}" for char, count in repeated_chars.items()])

    return repeated_chars_formatted

# Test the function
string = 'thequickbrownfoxjumpsoverthelazydog'

print(f"Repeated characters in {string} are: {count_repeated_characters(string)}")
