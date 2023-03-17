class Solution():
    def isValid(self, str):
        if str.count("(") == str.count(")") and str.count("{") == str.count("}") and str.count("[") == str.count("]"):

            return True
        else:
            return False

x = Solution()
x.isValid()
