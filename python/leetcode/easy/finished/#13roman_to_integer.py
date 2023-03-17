class Solution():
    def romanToInt(self, roman):
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for index, char in enumerate(roman):
            #if next char is smaller, add current char, else subtract current char
            if index == len(roman) - 1:
                total += dict[char]
            elif dict[char] >= dict[roman[index + 1]]:
                total += dict[char]
            else:
                total -= dict[char]
            print(total)
            return total

x = Solution()
x.romanToInt("III")