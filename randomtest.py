
# Here is a python function that can read in an encoded message from a .txt file and return the decoded version as a string:

def decode(message_file):
    # Reads an encoded message from a .txt file and returns the decoded version as a string
    dictionary = {}
    # unpacks the encoded message from a .txt file
    with open(f"{message_file}") as f:
        for count, line in enumerate(f):
            (key, val) = line.split()
            dictionary[int(key)] = val
    
    # decodes the message
    # gets the correct pyramid numbers
    numbers_needed = []
    total = 0
    increment = 1
    while total < count + 1:
        total += increment
        increment += 1
        numbers_needed.append(total)

    # returns message as a string
    words_list = []
    for num in numbers_needed:
        words_list.append(dictionary[num])
    final_message = " ".join(words_list)
    return final_message

"""
The function first creates an empty dictionary which will be used to save the key:value pairs from the .txt file.
It then opens the provided .txt file, counts the total amount of lines, and saves all the key:value pairs in the dictionary.
Afterwards, it determines the relevant numbers at the end of each pyramid line (1, 3, 6, etc.) while not going past the total line count of the .txt file and saves them in the numbers_needed list.
It does this by keeping track of how many numbers are in the line before it, adds one, and saves that number to the list, repeating until the total amount of lines in the .txt files is larger than the number.
Next, it creates an empty list that will keep track of the needed words.
It loops through the necessary numbers that were saved in the needed_numbers list and finds the corresponding word values, adding them to the words_list.
Finally, it joins all the words in the words_list together while separating them with a space, creating the final string message, and returning it.
"""


print(decode("coding_qual_input.txt"))