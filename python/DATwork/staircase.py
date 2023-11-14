def is_staircase(nums):
    col_length = 0
    staircase = []

    while len(nums) > 0:
        col_length = col_length + 1
        column = []

        for i in range(0, col_length):
            column.append(nums.pop(0))

            if (len(nums) == 0):
                if i < col_length - 1:
                    return False
                # staircase.append(column)
                return staircase
        staircase.append(column)


print(is_staircase([1, 2, 3, 4, 5, 6]))
print(is_staircase([1, 2, 3, 4, 5, 6, 7]))

def is_staircase2(nums):
    col_length = 0
    staircase = []
    input_list = nums.copy()

    while len(input_list) > 0:
        col_length = col_length + 1
        column = []

        for i in range(0, col_length):
            column.append(input_list.pop(0))

            if (len(input_list) == 0):
                if i < col_length - 1:
                    return False
                staircase.append(column)
                return staircase
        staircase.append(column)

print(is_staircase2([1, 2, 3, 4, 5, 6,]))
print(is_staircase2([1, 2, 3, 4, 5, 6, 7]))