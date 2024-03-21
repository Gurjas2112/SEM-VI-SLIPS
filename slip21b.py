#Write a Python function that takes a list of words and returns the longest word and its length

def find_longest_word(words):
    if not words:
        return None, 0

    longest_word = max(words, key=len)
    return longest_word, len(longest_word)

# Example of usage:
words_list = ["apple", "banana", "kiwi", "strawberry"]
longest_word, length = find_longest_word(words_list)
print(f"The longest word is '{longest_word}' with a length of {length}.")