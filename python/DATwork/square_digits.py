import decimal

import itertools

def square_digits(n):
    digits = [int(digit) for digit in str(n)]
    squared_digits = [int(''.join(map(str, group))) for _, group in itertools.groupby(digits, key=lambda x: x // 10)]
    return int(''.join(map(str, squared_digits)))


print(square_digits(123)) # 149