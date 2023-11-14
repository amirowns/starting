class Solution:
    def isPalindrome(self, number):
        return str(number) == str(number)[::-1]

x = Solution()
print(x.isPalindrome(121))