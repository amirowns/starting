class Solution():
    def longestCommonPrefix(self, lst):
        current_best = ""
        lst.sort(key=len)
        comparer = lst[0]
        still_good = False

        for x in range(0, 200):
            if current_best == comparer:
                    print(current_best)
                    return current_best
            for str in lst:
                if str[x] == comparer[x]:
                    still_good = True
                else:
                    print(current_best)
                    return current_best
            if still_good == True:
                current_best += comparer[x]
                print(current_best)


x = Solution()
x.longestCommonPrefix(["ab", "a"])


"""
cool approach uses zip to make a tuple of all the iterated letters, then uses set to see if they are all the same
current_best = ""
for x in zip(*strs):
    if len(set(x)) == 1:
        current_best += x[0]
    else:
        return current_best
    return current_best 
"""