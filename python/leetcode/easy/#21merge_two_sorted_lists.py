class Solution():
    def mergeTwoLists(self, lst1, lst2):
        lst1.extend(lst2)
        lst1.sort()
        return lst1


x = Solution()
x.mergeTwoLists([0,4,7,3],[2,4,7])