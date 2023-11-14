# Can you make a function using python that calculates the sum of the numbers in the nth row of a triangle that contains only consectuvie odd numbers starting at index 1?
# The first row of the triangle has the number 1.
# The second row has the numbers 3 and 5.
# The third row hs 7, 9, and 11.
# The next rows continue in this pattern.



# better
def row_sum_odd_numbers(n):
    #your code here
    return n ** 3

# muffin
def nth_row_sum(n): 
    return (3 * n * n - n) // 2

# banana
def sum_of_row(n):
    # Calculate the first number in the nth row
    first_num_in_row = 2*n - 1

    # Calculate the sum of the row
    sum_of_row = n * (first_num_in_row + first_num_in_row + 2*(n-1)) // 2

    return sum_of_row


print(row_sum_odd_numbers(-1)) # ?? 
print(row_sum_odd_numbers(1)) # 1 
print(row_sum_odd_numbers(2)) # 8 
print(row_sum_odd_numbers(3)) # 27 

"""
Sure, here is a simple Python function that calculates the sum of the numbers in the nth row of a triangle that contains only consecutive odd numbers starting at index 1:

def nth_row_sum(n):
    return n ** 3

Example usage:
print(nth_row_sum(1)) # 1
print(nth_row_sum(2)) # 8
print(nth_row_sum(3)) # 27

This function works by taking an integer, n, and returns the cube of this integer. When looking at the totals of each row in the pyramid, this pattern is found. For the first row, 1 = 1. For the second row, 3 + 5 = 8. For the third row, 7 + 9 + 11 = 27. This function will not work correctly if a non-integer number is given, or if an integer less than 1 is given.

I hope this helps! Let me know if you have any other questions.
"""
"""

"""