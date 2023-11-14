# Can you write a function using python that is given a string and converts the letters into either lowercase or uppercase, making as few changes as possible? If there is an equal amount, convert the letters to lowercase.


# muffin
def convert_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())

    if upper_count <= lower_count:
        return string.lower()
    else:
        return string.upper()

# banana
def convert_case(s):
    lower_case_count = sum(1 for c in s if c.islower())
    upper_case_count = sum(1 for c in s if c.isupper())
    return s.lower() if lower_case_count >= upper_case_count else s.upper()

# more efficient
def solve(s):
    upper = 0
    lower = 0
    for x in s:
        if x.islower():
            lower +=1
        elif x.isupper():
            upper +=1
    if upper > lower:
        return s.upper()
    return s.lower()


print(solve("h3o2wd7Y!  Yall"))

"""
Sure, here is a function using Python that converts the letters in a string into either lowercase or uppercase, making as few changes as possible:

def convert_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return string.lower() if upper_count <= lower_count else return string.upper()

Example usage:
print(convert_case("Hello, World!")) # hello, world!
print(convert_case("H1O2W  3d4y5!)) # H1O2W  3D4Y5!

This function works by first initializing two variables to keep track of the count of upper and lower case letters in the given string. It does this by first looping through the string and checking if each character is an uppercase letter for the first variable, or a lowercase letter for the second variable, adding a 1 to a generator object if it is. Then, the sum of the generator object is calculated to find the count of uppercase or lowercase letters. Finally, the variables are compared to each other, and the entire string gets converted to uppercase or lowercase depending on which variable has a higher count. While this function is easy to read, it has a total of 4 loops, and is not as efficient as the following function:

def solve(s):
    upper = 0
    lower = 0
    for x in s:
        if x.islower():
            lower +=1
        elif x.isupper():
            upper +=1
    if upper > lower:
        return s.upper()
    return s.lower()

This function only loops through the string once, checking each character to see if it is uppercase or lowercase and updating the corresponding variable. Afterward, the variable with the higher count has the entire string converted to uppercase or lowercase. 

I hope this helps! Let me know if you have any other questions.
"""
"""
This response is better than Muffin's and Banana's responses because it includes an example with a concise answer, showing edge cases, as well as including a more efficient function, describing why it is more efficient. It also has a very in-depth explanation of what is happening with the original function.
"""