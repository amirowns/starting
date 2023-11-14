# Can you write a function using python that is given two integers and returns the count of all numbers between these two integers, except for numbers with a 5 in them. The two given integers should also be included.



# muffin
def count_without_five(start, end):
    # Check if start and end are valid integers
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")

    # Ensure start is less than or equal to end
    if start > end:
        raise ValueError("start must be less than or equal to end")

    count = 0
    for num in range(start, end + 1):
        if '5' not in str(num):
            count += 1

    return count


# banana
def count_numbers_without_five(start, end):
    count = 0
    for i in range(start, end + 1):
        if '5' not in str(i):
            count += 1
    return count


# better
def count_without_five2(a, b):
    return sum('5' not in str(i) for i in range(min(a, b), max(a, b) + 1))

print(count_without_five2(9, 9))



"""
Sure, here is a Python function that counts all numbers between two integers, except for numbers with a 5 in them, including the given integers:

def count_without_five(a, b):
    return sum('5' not in str(i) for i in range(min(a, b), max(a, b) + 1))

Example usage:
print(count_without_five(1, 6)) # 5
print(count_without_five(9, 6)) # 4

This function works by looping through the integers starting from the lower given integer, found by using the min() function and stopping at the higher given integer, found by using the max() function.
During each loop, the integer is turned into a string and is checked to see if the string "5" is contained in it.
If it is not in the number, the statement is determined as True, which is equivalent to 1.
If "5" is in the number, the statement is determined as False, which is equivalent to 0.
The number equivalent of these True and False values are then summed up to return the total count of numbers without a 5 in them.

I hope this helps! Let me know if you have any other questions.
"""
"""
This response is better than Muffin's response because it does not redundantly check if the given integers are integers since it is specified that integers are given.
This response is also better than Muffin's and Banana's responses because it is also able to give the correct answer if the first integer is more than the second integer, not returning an error or incorrect answer.
On top of this, there are examples given showing that it correctly avoids "5"s, and works whichever way the integers are given.
"""