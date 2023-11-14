# Can you write a function using python that is given an integer and rounds it to the next multiple of 5?


# muffin
def round_to_next_multiple_of_5(num):
    remainder = num % 5
    if remainder == 0:
        return num
    else:
        return num + (5 - remainder)



# banana
def round_to_next5(n):
    if n % 5 == 0:
        return n
    else:
        return n + (5 - n % 5)



# better
def round_to_next52(n):
    return n + (-n % 5)


print(round_to_next52(-3))



"""
Sure, here is a simple Python function that rounds an integer to the next multiple of 5:

def next_multiple_of_5(n):
    return n + (-n % 5)

Example usage:
print(next_multiple_of_5(10)) # 10
print(next_multiple_of_5(3)) # 5

This function works because of how Python handles negative numbers while using the modulo operator.
In Python, mod = n - math.floor(n / base) * base. Using the above example where n = 3, the function calculates (-n % 5) as follows:
mod = -3 - math.floor(-3 / 5) * 5
mod = -3 - math.floor(-0.6) * 5
mod = -3 - (-1 * 5)
mod = 2
Then, add n to this, resulting in 3 + 2 = 5.

I hope this helps! Let me know if you have any other questions.
"""
"""
This response is better than Muffin's response because it is simpler, doesn't need an if-else statement, has an in-depth explanation, and provides a more concise example with an answer.
This response is also better than Banana's response because of the simpler function without needing an if-else statement.
"""