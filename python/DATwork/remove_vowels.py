def remove_vowels(text):
    vowels = 'aeiou'
    return ''.join([c for c in text if c not in vowels])

print(remove_vowels("Hello WOrld!"))


import re
import unicodedata

def remove_vowels2(s):
    vowels = 'aeiouAEIOU'
    # Add accented characters
    vowels += 'áéíóúÁÉÍÓÚ'
    # Add non-ASCII characters
    vowels += '\u4e00-\u9fa5'  # Chinese characters
    vowels += '\u3040-\u309f'  # Japanese characters
    # ... add more non-ASCII ranges as needed

    # Use the unicodedata module to normalize the string
    s = unicodedata.normalize('NFKC', s)

    # Remove vowels using the updated vowels variable
    return ''.join([c for c in s if c not in vowels])

print(remove_vowels2("Hello World"))
print(remove_vowels2("CaféHello World"))
print(remove_vowels2("ngHello World"))
print(remove_vowels2( "こんにちは"))
print(remove_vowels2("Hello World"))