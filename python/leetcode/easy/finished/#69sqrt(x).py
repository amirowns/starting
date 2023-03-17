class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        counter = 0
        for i in range(1, x + 1):
            if i * i <= x:
                counter += 1
            else:
                print(counter)
                return counter


w = Solution()
w.mySqrt(1)