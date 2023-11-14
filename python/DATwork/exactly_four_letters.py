# Can you write a function using python that takes in a list of strings and returns the strings that have exactly 4 letters in them?

# better
import re

def friend(arr):
  return [x for x in arr if re.match('^([^a-zA-Z]*[A-Za-z]){4}[^a-zA-Z]*$', x)]

print(friend(["1Ch^", "!!held", "sure", "nopers", "good1", "1a2b3c4d5"]))


# banana
def four_letter_words(lst):
    return [word for word in lst if len(word) == 4]

# print(four_letter_words(["1Ch^"]))


# muffin
def filter_four_letter_words(words):
    four_letter_words = []
    for word in words:
        if len(word) == 4:
            four_letter_words.append(word)
    return four_letter_words


def four_letter_strings2(strings):
    return [x for x in strings if re.match('^(?:([A-Za-z]){4})?[^a-zA-Z]*$', x)]

print(four_letter_strings2(["1Ch^", "!!held", "sure", "nopers", "good1", "1a2b3c4d5"]))