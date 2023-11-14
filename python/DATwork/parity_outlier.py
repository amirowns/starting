
def find_outliers(integers):
    """
    Finds the outlier in a list of integers that are all odd or all even except for one.

    Args:
    numbers: A list of integers.

    Returns:
    The outlier integer.
    """
    parity = [n % 2 for n in integers]
    return integers[parity.index(sum(parity) == 1)]
 

def find_outlier(numbers):
    even_count = 0
    odd_count = 0
    majority_parity = None
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if even_count > odd_count:
            majority_parity = 0
        elif odd_count > even_count:
            majority_parity = 1
        if num % 2 != majority_parity:
            return num
    return None



print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])) # 11
print(find_outlier([160, 3, 1719, 19, 11, 13, -21])) # 160