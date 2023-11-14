# Can you write a function using python that takens an integer greater than 1 and returns an array with all of the integer's divisors, except for 1 and itself, from smallest to largest?




# muffin
def find_divisors(n):
    if n <= 1:
        raise ValueError("Input must be an integer greater than 1")

    divisors = []
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)

    return divisors


# banana
def find_divisors2(n):
    divisors = []
    for i in range(2, n):
        if (n % i) == 0:
            divisors.append(i)
    return divisors


# better
def divisors(num):
    return [i for i in range(2, num // 2 + 1) if (num % i) == 0]


def divisors2(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return [p for p in range(2, n+1) if sieve[p]]


print(divisors(36))
print(divisors2(36))


"""
Sure, here is a Python function that takes an integer greater than 1 and returns an array with all of the integer's divisors, except for 1 and itself, from smallest to largest:

def find_divisors(num):
    return [i for i in range(2, num // 2 + 1) if (num % i) == 0]

Example usage:
print(find_divisors(12)) # [2, 3, 4, 6]
print(find_divisors(13)) # []

This function works by looping through the integers starting from 2 and stopping at half the given integer, rounded down, plus one.
The reason for this is that 1 is excluded, and the maximum integer that could be a divisor is half the given integer. Each of these integers is checked to see if the given integer modulo the current integer equals zero, making it a divisor, and adds it to the returned list if it is. 

I hope this helps! Let me know if you have any other questions.
"""
"""
This response is better than Muffin's response because the prompt specifically states that an integer greater than 1 is given, so it is redundant to check if the integer would be greater than 1. Additionally, the example's answer is written in-line as a comment to have easier readability. 
This response is better than Muffin's and Banana's responses because it is more efficient, looping through approximately half the amount of integers to find the correct answer.
"""