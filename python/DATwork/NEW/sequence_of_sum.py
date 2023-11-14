# Your task is to write a function using python which returns the sum of a sequence of integers.
# The sequence is defined by 3 non-negative values: begin, end, step.
# If begin value is greater than the end, your function should return 0.
# If end is not the result of an integer number of steps, then don't add it to the sum.



"""
# summation formula, summing 0 to n
n * (n + 1) / 2

# summation formula, summing 0 to n with steps
(n//divisor * (n//divisor + 1) / 2) * divisor

# summation formula, accounting for a different begin
diff = end - begin
begin * (diff // step + 1) + (diff // step * (diff // step + 1) / 2) * step

# simplifies diff // step to stride
stride = diff // step
begin * (stride + 1) + (stride * (stride + 1) / 2) * step

# re-organizes
((stride + 1) * begin) + ((stride + 1) * stride / 2 * step)

# taking out the common factor, (stride + 1)
(stride + 1) * (begin + (stride / 2 * step))
"""    


# better
def sequence_sum(begin, end, step):
    stride = (end - begin) // step
    return 0 if begin > end else (stride + 1) * (begin + (stride / 2 * step))


# muffin
def sequence_sum2(begin, end, step):
    if begin > end:
        return 0

    if end % step != 0:
        end = end - (end % step)

    return sum(range(begin, end + 1, step))



# banana
def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    else:
        total = 0
        for i in range(begin, end + 1, step):
            total += i
        return total


print(sequence_sum2(2, 10, 2))

"""
Sure, here is a simple Python function that calculates the sum of a sequence of integers:

def sequence_sum(start, end, step):
    return sum(range(start, end+1, step))

Example usage:
print(sequence_sum(2, 10, 2))  # 30
print(sequence_sum(5, 3, 1))  # 0
print(sequence_sum(1, 15, 3))  # 35

This function uses the built-in sum() function to calculate the sum of the sequence of integers given by using the range() function which takes the begin, end, and step arguments. If the begin value is greater than the end value, 0 is returned. While this function is easy to read, its efficiency can be improved upon with the following function:

def sequence_sum(begin, end, step):
    stride = (end - begin) // step
    return 0 if begin > end else (stride + 1) * (begin + (stride / 2 * step))

This function derives from the Gauss Summation formula to mathematically calculate the answer, returning 0 if the begin value is greater than the end value.

The Gauss Summation formula:
n * (n + 1) / 2
This formula calculates the sum of all integers starting from 0 and ending at n.
When steps are included, the formula becomes:
(n // step * (n // step + 1) / 2) * step
This formula calculates the sum of all integers starting from 0 and ending at n while skipping every step numbers.
When a new starting value is introduced, the formula becomes:
((end - begin) // step * ((end - begin) // step + 1) / 2) * step + begin * ((end - begin) // step + 1)
This formula calculates the sum of all integers starting from begin and ending at end while skipping every step numbers.
Since ((end - begin) // step) occurs multiple times, it can be simplified:
stride = (end - begin) // step
(stride * (stride + 1) / 2) * step + begin * (stride + 1)
After reorganizing it becomes:
stride = (end - begin) // step
((stride + 1) * stride / 2 * step) + ((stride + 1) * begin)
From here, the common factor (stride + 1) can be taken out:
stride = (end - begin) // step
(stride + 1) * (begin + (stride / 2 * step))

I hope this helps! Let me know if you have any other questions.
"""
"""
This response is better than Muffin's and Banana's responses because it has an easier-to-read function, as well as a higher performance function without redundancies.
This response also has an in-depth explanation and examples with correct answers.
Muffin's response has some redundancies that don't need to be checked, as well as an incorrect example answer, while the code actually works.
Banana's response is lacking an example.
"""