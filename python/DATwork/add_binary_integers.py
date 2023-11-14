# Can you write a function using python that adds two integers together and returns their sum in binary as a string?

from time import perf_counter

# better
def add_binary(a,b):
    return f"{a + b:b}"

# banana
def add_binary2(a, b):
    sum = a + b
    return bin(sum)[2:]

# muffin
def add_integers_binary(a, b):
  """Adds two integers and returns their sum in binary as a string."""
  sum = a + b
  binary_sum = bin(sum)[2:]
  return binary_sum


def add_ints_binary(a, b):
    return bytes((a + b).to_bytes((a + b).bit_length(), byteorder='big')).decode()


start_time = perf_counter()

print(add_binary(10, 20)) # 1111
print(add_binary(1, -4)) # -11

passed_time = perf_counter() - start_time

print(f"It took {passed_time * 1000} ms")

"""
Sure, here is a simple Python function that adds two integers together and returns their sum in binary as a string: 

def add_integers_binary(a, b):
    return f"{a + b:b}"

Example usage:
print(add_binary(1, 7)) # 1000
print(add_binary(1, -9)) # -11

This function uses f-strings to add the integers together and return the answer converted into binary.
The ":b" section is what converts the sum into binary. Other options are available as well, such as "{a + b:X}" for hexadecimal or "{a + b:o}" for octal formatting.

I hope this helps! Let me know if you have any other questions.
"""
"""
This response is better than both Muffin's and Banana's responses because it can accurately deal with negative integer sums, and uses a more updated method that looks cleaner to read.
The problem with these models' responses is that the bin() function will return a negative integer sum in binary format with a prefix of "-0b" instead of "0b" which the models handle well for positive integer sums. 
This leads to incorrectly answering the negative integer sums.
"""
