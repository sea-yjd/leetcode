# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        # solution 1:
        # num = 0
        # roman = {'I': 1, 'IV': 4, 'V': 5,  'IX': 9, 'X': 10,  'XL':40, 
        #               'L': 50,  'XC':90,  'C': 100,  'CD': 400,  'D': 500,  'CM': 900, 'M': 1000}
        # i = 0
        # while i < len(s):
        #     if s[i:i+2] in roman.keys():
        #         num += (roman.get(s[i:i+2]))
        #         i = i+2
        #     else:
        #         num += (roman.get(s[i]))
        #         i += 1
        # return num
        ## solution 2:
        number_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(0,len(s)):
            if i > 0 and number_map[s[i]] > number_map[s[i-1]]:
                result += (number_map[s[i]] - 2*number_map[s[i-1]])
            else:
                result += number_map[s[i]]
                
        return result
S = Solution()
y = S.romanToInt("MCMXCIV")
print(y)
