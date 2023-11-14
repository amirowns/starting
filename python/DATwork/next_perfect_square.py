# Can you write a function using python that is given an integer and returns the next perfect square after this integer?


# banana
import math

def next_perfect_square(n):
    # Calculate the square root of n
    sqrt_n = math.sqrt(n)
    # Take the ceiling of sqrt_n to get the next integer
    next_n = math.ceil(sqrt_n)
    # Square next_n to get the next perfect square
    next_perfect_square = next_n ** 2
    return next_perfect_square

# print(next_perfect_square(9))


# muffin
import math

def next_perfect_square2(n):
    # Check if n is a perfect square
    if math.sqrt(n) % 1 == 0:
        # If n is a perfect square, find the next perfect square
        next_square = (math.sqrt(n) + 1) ** 2
    else:
        # If n is not a perfect square, find the first perfect square greater than n
        next_square = math.ceil(math.sqrt(n)) ** 2

    return next_square

# print(next_perfect_square2(-9))

# what if negative integer given?
# return integer not float
from math import sqrt, ceil

def next_perfect_square3(n):
    # Check if n is a perfect square
    if n < 1:
        return 1
    
    root = sqrt(n)

    if root % 1 == 0:
        # If n is a perfect square, find the next perfect square
        next_square = int((root + 1) ** 2)
    else:
        # If n is not a perfect square, find the first perfect square greater than n
        next_square = ceil(root) ** 2

    return next_square


#better
from math import sqrt, ceil

def next_perfect_square4(n):
    # Check if n is a perfect square
    if n < 1:
        return 1
    root = sqrt(n)
    return int((root + 1) ** 2) if root % 1 == 0 else ceil(root) ** 2


print(next_perfect_square4(-4))
print(next_perfect_square4(9))
print(next_perfect_square4(8))
SQRT_1 = sqrt(1)
def next_perfect_square5(n):
    if n < 1:
        return 1
    root = sqrt(n)
    return int(root + 1) ** 2 if root % 1 == 0 else int(root + SQRT_1) ** 2

print()
print(next_perfect_square5(-4))
print(next_perfect_square5(9))
print(next_perfect_square5(15))


"""
Sure, here is a simple Python function that is given an integer and returns the next perfect square after this integer:

from math import sqrt, ceil

def next_perfect_square(n):
    if n < 1:
        return 1
    root = sqrt(n)
    return int((root + 1) ** 2) if root % 1 == 0 else ceil(root) ** 2

Example usage:
print(next_perfect_square(-4)) # 1
print(next_perfect_square(8)) # 9
print(next_perfect_square(9)) # 16

This function works by first checking whether the given integer is less than 1, and returns 1 if it is. This is necessary to avoid an error caused by trying to find the square root of a negative number. Next, the square root of the integer is calculated using the math.sqrt() function. Then, if this root % 1 == 0, it means the integer is already a perfect square, so 1 gets added to the root and the next perfect square is found and turned into an integer, instead of returning as a float. In the case the integer is not a perfect square already, the root gets rounded up using the math.ceil() function, and the next perfect square is returned.

I hope this helps! Let me know if you have any other questions.
"""


"""
This response is better than Muffin's because it takes into account if the given integer is negative, returning 1 instead of an error. It also only imports the required functions from the math library, and stores the root of the integer as a variable, rather than running the function twice, making it more efficient time-wise. There are also a few examples to show what should happen.
This response and Muffin's are better than Banana's because in the case where the integer is already a perfect square, they find the next perfect square, rather than Banana's returning the same perfect square. Banan also has problems with negative integers.
"""