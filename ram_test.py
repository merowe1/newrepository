
def is_isogram(word):
    word = word.lower()  # Convert the word to lowercase to make the comparison case-insensitive
    unique_letters = set(word)  # Convert the word to a set to remove duplicates
    return len(word) == len(unique_letters)

print(is_isogram("isogram"))  # True
print(is_isogram("uncopyrightable"))  # True
print(is_isogram("ambidextrously"))  # False (repeated letters: 'a', 'b')
