"""
Can you write a function in Python that is given a string of text and returns a list of the top 3 most occurring words in descending order of the number of occurrences?
Words including an apostrophe such as "won't" should also be included.
Capitalization doesn't matter, return them in lowercase.
If there is a tie, return the first word that occurs.
A word surrounded by non-letters should also be included.
For example, "  ''' //wont Won't won't " should return ["won't", "wont"].
"""
# better answer
import collections
import re

def top_3_words(text):
    word_count = collections.Counter(re.findall(r"[a-z']+", re.sub(r"\W+'+\W+", " ", text.lower())))
    return [word for word, count in word_count.most_common(3)]


# Banana
import collections
import re

def top_three_words(text):
    # Use a regular expression to replace non-alphabetic characters
    words = re.findall(r'\b\w+\b', text.lower())
    # Use a Counter to count the occurrences of each word
    word_counts = collections.Counter(words)
    # Find the three most common words
    top_three = word_counts.most_common(3)
    # Return only the words, not their counts
    return [word for word, count in top_three]



# Muffin
from collections import Counter

def top_three_most_occuring_words(text):
  """Returns a list of the top 3 most occurring words in descending order of the number of occurrences.

  Args:
    text: A string of text.

  Returns:
    A list of the top 3 most occurring words in descending order of the number of occurrences.
  """

  word_counts = Counter(text.split())
  top_three_words = word_counts.most_common(3)
  return [word for word, count in top_three_words]


def top_three_words2(text):
    # Use regular expressions to find all words, including contracted ones
    words = re.findall(r"[a-z']+", text)
    words = [re.sub(r'[^a-z]', '', word) for word in words]
    words = [word.lower() for word in words]  # Convert to lowercase
    # Create a counter to count the occurrences of each word
    counter = collections.Counter(words)
    # Get the top 3 most occurring words and sort them in descending order
    top_words = sorted(counter.most_common(3), key=lambda x: x[1], reverse=True)
    # Return the list of top 3 words
    return [word for word, count in top_words]




print(top_3_words("  ''' //wont Won't won't ")) # ["won't", "wont"]
print(top_3_words("This is a sample text with some repeated words."))
print(top_3_words("This isn't a sample text,' this is 1 of the sample texts."))