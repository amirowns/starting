# determines if a number is even
def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
# determines if a number is an integer
def is_int(x):
  if x == round(x):
    return True
  else:
    return False
# determines the sum of the digits
def digit_sum(n):
    total = 0
    nstring = str(n)
    for num in nstring:
        
        total += int(num)
    return total
# determines the factorial of a number
def factorial(x):
    total = x
    while x > 1:
        x -= 1
        total = total * x
    return total
# determines if a number is prime # this one gave me a rough time
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x - 1):
            if x % n == 0:
                return False
        else:
            return True
# print the reverse of a string
def reverse(text):
    newtext = ""
    for char in text:
        newtext = char + newtext
    return newtext
# removes the vowels and returns the string
def anti_vowel(text):
    newstring = text
    for char in text:
        if char == "A" or char == "a" \
            or char == "E" or char == "e" \
            or char == "I" or char == "i" \
            or char == "O" or char == "o" \
            or char == "U" or char == "u":
                newstring = newstring.replace(char, "")
            
    return newstring
# gives the scrabble value of a word
def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
            "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
            "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
            "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
            "x": 8, "z": 10}

    points = 0

    for letter in word:
        points += score[letter.lower()]
    print(word, points, "points")
    return points 
# replaces a certain string everytime it occurs in a given string
def censor(text, word):
    asteriskify = word
    sentence = text
    for char in word:
        asteriskify = asteriskify.replace(char, "*")
    sentence = sentence.replace(word, asteriskify)
    return sentence
# counts amount of item in a listed sequence
def count(sequence, item):
    counter = 0
    for char in sequence:
        if char == item:
            counter += 1
    return counter
# removes all odd numbers from a list
def purify(numbers):
    evenlist = []
    for num in numbers:
        if num % 2 == 0:
            evenlist.append(num)
    return evenlist
# multiplies each integer in the list
def product(intlist):
    total = 1
    for num in intlist:
        total = total * num
    return total
# removes duplicates in a list
def remove_duplicates(_list):
    newlist = set(_list)
    return newlist
# finds the median in a list
def median(_list):
    newlist = sorted(_list)
    # if list is even
    if len(newlist) % 2 == 0:
        newnewlist = [newlist[int(len(newlist) / 2)], newlist[int(len(newlist) / 2 - 1)]]
        #avg middle 2
        total = 0
        for num in newnewlist:
            total += num
        total = total / 2
        return total
    else:
        newnewlist = newlist[int((len(newlist) - 1) / 2)]
        return newnewlist
# converts RGB to Hex
def RGB_to_Hex(r, g, b):
    Hex_value = f'{r:02x}{g:02x}{b:02x}'
    return Hex_value
# converts Hex to RGB 
def Hex_to_RGB(input):
    RGB_value = (int(input[:2], 16), int(input[2:4], 16), int(input[4:], 16))
    return RGB_value
