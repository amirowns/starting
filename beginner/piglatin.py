
ending = "ay"
original = input("Please enter a word or phrase: ")
originalsplit = original.split()

if len(original) > 0 and len(originalsplit) == 1 : # and original.isalpha: 
    word = original.lower()
    first_letter = word[0]
    new_word = word + first_letter + ending
    new_word = new_word[1:len(new_word)]
    print (new_word)
# the above turns 1 word into piglatin, now to make a phrase

elif len(originalsplit) > 1 : # and original.isalpha:
    lowercase = original.lower()
    phrase = lowercase.split()
    # how do i call each word and apply piglatin to each one, come back when i can loop it?
   
    """def capitalize_word(originalsplit):
        return originalsplit[:1].capitalize() + originalsplit[1:].lower()
    originalsplit = [s.strip() for s in originalsplit]
    originalsplit = [capitalize_word(s) for s in originalsplit]"""

    def piglatinify(originalsplit):
         return originalsplit[1:] + originalsplit[:1] + ending

    originalsplit = [piglatinify(s) for s in originalsplit]

    originalsplit = " ".join(originalsplit)
    print(originalsplit)

else: print ("You didn't enter a word")



