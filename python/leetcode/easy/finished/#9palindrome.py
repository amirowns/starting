class Solution:
    def isPalindrome(self, number):
        print(str(number) + " " + str(number)[::-1]) 
        if str(number) == str(number)[::-1]:
            return True
        else: 
            return False

x = Solution()
print(x.isPalindrome(-121))