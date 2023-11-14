Sure, here is a function that does this:

```python
import collections
import re

def top_3_words(text):
    word_count = collections.Counter(re.findall(r"[a-z']+", re.sub(r"\W+'+\W+", " ", text.lower())))
    return [word for word, count in word_count.most_common(3)]
```

This function uses the `re.sub` function to search the lowercase version of the given text `text.lower()` for the occurences where there are one or more non-word characters followed by one or more apostrophes followed by one or more non-word characters `"\W+'+\W+"` and replaces them with a space. In your example of the text `" ''' //wont Won't won't "`, this would match `" ''' //"`and turn the text into`" wont Won't won't "`. Then, the `re.findall` function would search this new string for all occurences where there are one or more letters or apostrophes `"[a-z']+"` and keep them in a list. Next, the `collections.Counter` function uses the list to keep track of the different words and their respective occurrences in a dictionary `word_count`. Finally, the `most_common` function is used on this dictionary to return the 3 most common words and their amount of occurences as a tuple and is looped through to return just the words as a list in order.

Sure, I can do that for you.

1. The `re.sub` function searches the lowercase version of the given text `text.lower()` for the regular expressions pattern `"\W+'+\W+"` which matches one or more non-word characters followed by one or more apostrophes followed by one or more word characters and replaces these instances with a space `" "`, returning a new string.

2. The `re.findall` function searches this new string for the regular expressions pattern `"[a-z']+"` which matches one or more letters or apostrophes and returns all these instances as a list.

3. The `collections.Counter` function creates a dictionary, using each element of the list as the keys and the counts of the elements as the values.

4. This dictionary is then set to the variable `word_count`.

As an example, let the given text be `"This isn't a sample text,' this is 1 of the sample texts."`

1. In the `re.sub` function the text would be converted to lowercase, then searched for the `"\W+'+\W+"` pattern which matches `[",' ", " 1 "]`, replacing them with a space `" "`. This would return `"this isn't a sample text this is of the sample texts."`

2. The `re.findall` function searches this string for the pattern `"[a-z']+"` which matches `['this', "isn't", 'a', 'sample', 'text', 'this', 'is', 'of', 'the', 'sample', 'texts']` and returns this list.

3. The `collections.Counter` function creates a dictionary from this list. `Counter({'this': 2, 'sample': 2, "isn't": 1, 'a': 1, 'text': 1, 'is': 1, 'of': 1, 'the': 1, 'texts': 1})`

4. This dictionary then gets assigned to the `word_count` variable.
