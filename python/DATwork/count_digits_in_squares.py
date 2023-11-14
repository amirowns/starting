# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.
# Square all numbers k (0 <= k <= n) between 0 and n.
# Count the numbers of digits d used in the writing of all the k**2.
# Implement the function using python taking n and d as parameters and returning this count.


# muffin
def count_digits(n, d):
    count = 0
    for k in range(n + 1):
        k_squared = k * k
        for digit in str(k_squared):
            if int(digit) == d:
                count += 1
    return count


# banana
def count_digit_squares(n, d):
    count = 0
    for k in range(n+1):
        count += str(k**2).count(str(d))
    return count


# better
def nb_dig(n, d):
    return str([n**2 for n in range(n + 1)]).count(str(d))

print(nb_dig(5, 2))


"""
Sure, here's a Python function that takes an integer n (n >= 0) and a digit d (0 <= d <= 9) as parameters and returns the count of digits d used in the writing of all the k**2 for 0 <= k <= n:

def count_digits(n, d):
  return str([n**2 for n in range(n + 1)]).count(str(d))

Example usage:
print(count_digits(10, 1)) # 4
print(count_digits(25, 1)) # 11

This function works by first looping through the range of 0 to n + 1, creating a list of all the squares of these integers, and then converting the entire list into a string. The count() function then searches this string for every occurrence of the given digit, d, in string form, and returns this number. 

In the above example, the k**2 from 0 to 10 are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100.
The digit 1 appears in 1, 16, 81, 100. Thus, the total count is 4.

I hope this helps! Let me know if you have any other questions.
"""
"""
This response is better than Muffin's response because it uses a lower time complexity, making it more efficient, explains how the function works, as well as having an answer given for the example. This response is also better than Banana's response because it is more efficient and has a lower time complexity. This is because Banana's response applies the count() function every iteration of the loop, while this response only applies the count() function once after the string is created.
"""