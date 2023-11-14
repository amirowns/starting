# Muffin
def middle_char(word):
  """Returns the middle character of the given word.

  If the word has an even length, the middle two characters are returned.

  Args:
    word: The word to find the middle character of.

  Returns:
    The middle character(s) of the word.
  """

  length = len(word)
  middle_index = length // 2

  if length % 2 == 0:
    # Even length word
    return word[middle_index - 1] + word[middle_index]
  else:
    # Odd length word
    return word[middle_index]
  
# print(middle_char("abcde")) # c
# print(middle_char("abcde ")) # cd
# print(middle_char("python")) # th


# best
def middle_char(s):
  i = (len(s) - 1) // 2
  return s[i:-i] or s



def middle_chars(s):
    length = len(s)
    middle_index = length // 2
    return s[middle_index:middle_index + (length % 2 != 0) - (length % 2 == 0)]

print(middle_chars("abcde")) # c
print(middle_chars("abcde ")) # cd
print(middle_chars("python")) # th