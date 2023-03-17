class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        example = s.split()
        print(len(example[-1]))

x = Solution()
x.lengthOfLastWord("luffy is still joyboy")