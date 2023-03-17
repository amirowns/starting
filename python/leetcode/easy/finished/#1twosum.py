
class Solution:
    def twoSum(self, nums, target):
        #grab first index and add index after, if it doesnt work, grab the next index
        # if none of those work, start with next index, and repeat
        #takes a while, but gets it done
        for index, number in enumerate(nums):
            for index_two, number_two in enumerate(nums):
                z = number + number_two
                if index == index_two:
                    pass
                elif z == target:
                    return [index, index_two]
            
    def twoSum_2(self, nums, target):
        #refactored to remove the number once it has been tried and found it doesnt work from the list to save some time
        for i in range(len(nums)):
            for index, number in enumerate(nums):
                z = nums[0] + number
                if nums.index(nums[0]) == index:
                    pass
                elif z == target:
                    return [i, i + index]
            del nums[0]

    def twoSum_3(self, nums, target):
        #refactored to remove numbers if they are too big or small
        copy = list(nums)
        for i in range(len(nums)):
            if target > max(nums) + min(nums):
                del nums[nums.index(min(nums))]
            elif target < max(nums) + min(nums):
                del nums[nums.index(max(nums))]
            else: 
                break

        for i in range(len(nums)):
            for index, number in enumerate(nums):
                z = nums[0] + number
                if nums.index(nums[0]) == index:
                    pass
                elif z == target:
                    ans_one = copy.index(nums[0])
                    ans_two = copy.index(number, ans_one + 1)
                    return [ans_one, ans_two]
            del nums[0]
        
    def twoSum_3(self, nums, target):
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]],i]
            else:
                required[nums[i]]=i


x = Solution()
print(x.twoSum_3([1,6,6,4,5,7], 12))
# expected: [1, 2]

