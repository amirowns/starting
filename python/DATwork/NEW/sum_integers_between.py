# Can you help me write a function in python that is given two integers and finds the sum of all the integers between and including them?


#better
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2 if a != b else a*2

print(get_sum(5, 1)) # 15
print(get_sum(2, 2)) # 2


#banana
def sum_between(a, b):
    return sum(range(a, b+1))

# print(sum_between(5, 1)) # 15


#muffin
def sum_integers(start, end):
    if start > end:
        raise ValueError("Start value cannot be greater than end value")

    total_sum = 0
    for num in range(start, end + 1):
        total_sum += num

    return total_sum

print(sum_integers(2, 2)) # 4
print(sum_integers(5, 1)) # 15


"""
Sure, here is a simple Python function that calculates the sum of all integers between and including two given integers:

def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2 if a != b else a*2

Example Usage:
print(get_sum(7, 2)) # 27

This function works by using the Gauss Summation formula to extrapolate the answer. The Gauss Summation formula is the total sum equals the number of pairs multiplied by the sum of each pair and that total is divided by two.

2 3 4 5 6 7
7 6 5 4 3 2
------------
9 9 9 9 9 9

This example can be used to show the idea that you can make two rows lining up the integers, one in ascending order, and the other in descending order. The sum of each pair of integers is 9, (a + b), and the number of times this occurs is 6, (abs(a-b) + 1). The absolute value is used here because the order of the integers is unknown, and this achieves the same result as a greater value minus a lower value. Multiplying these two values together, 9 * 6, results in 54, which needs to be divided by two because two of each digit was used. The final result ends up as 27. This formula does not work when the integers have the same value, so an if-else statement is used in the case where the integers are the same, returning the two integers added together.

I hope this helps! Let me know if you have any other questions.
"""
"""
This response is better because Muffin's response only returns a correct answer when the integers are given in descending order, otherwise raising an error, as well as incorrectly returning an answer when the integer values are the same. On top of this, Muffin's response uses a for loop, giving it a higher time complexity, and has no example to show how the function is used.
Banana's response also includes most of these problems, but is better in that it returns 0 if the integers are given in descending order, not returning an error, and having a more readable and efficient code than Muffin, using the sum() function.
This response is even better than Banana's as well because the solution doesn't use a loop at all, giving it a lower time complexity and higher efficiency, on top of the previously mentioned problems.
"""