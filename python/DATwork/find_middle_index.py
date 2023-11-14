# Can you write a function using python that is given three integers in an array and returns the index of the numerical element that lies between the other two elements? For example, [2, 3, 1] should return 0, because 2 is between 1 and 3, and has an index of 0.


# muffin
def find_middle_index(nums):
    # Sort the array
    sorted_nums = sorted(nums)

    # Find the index of the middle element in the original array
    for i, num in enumerate(nums):
        if num == sorted_nums[1]:
            return i

    # If no middle element is found, raise an error
    raise ValueError("Invalid input: Array does not contain a middle element")


# banana
def middle_index(nums):
    sorted_nums = sorted([(value, index) for index, value in enumerate(nums)])
    return sorted_nums[1][1]


# better
def gimme(nums):
    return nums.index(sorted(nums)[1])

print(gimme([2, 3, 1]))


def find_middle_index2(arr):
    sorted_arr = sorted(arr[:])  # create a new sorted list without mutating the original array
    mid = sorted_arr[1]  # middle element is the second element after sorting
    return arr.index(mid)  # find the index of the middle element in the original array


print(find_middle_index2([2, 3, 1]))



"""
Sure, here is a simple Python function that returns the index of the numerical element that lies between the other two elements in a given array of three integers:

def find_middle_index(nums):
    return nums.index(sorted(nums)[1])

Example Usage:
print(find_middle_index([2, 3, 1])) # 0
print(find_middle_index([5, 10, 14])) # 1

This function works by first determining what the correct numerical element is, sorting the given array in ascending order using the sorted() function and taking the middle element at index 1. Then, the index() function searches the given array for the first occurrence of this value and the index is returned. It should be noted that if the given integers are not unique, then the index at the first occurrence is returned.

I hope this helps! Let me know if you have any other problems!
"""
"""
This response is better than Muffin's response because it is cleaner and easier to read, provides examples, and does not include redundant code of raising an error since the prompt states an array of three integers is given, so there will always be a middle element found. This response is also cleaner and easier to read than Banana's response.
"""