def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")


def count_vowels(string):
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    
    vowels = {'a', 'e', 'i', 'o', 'u'}  # You can use the Unicode-aware vowels here instead
    string = string.lower()
    return sum(1 for char in string if char in vowels)


print(count_vowels("Hello WOrld")) # 3