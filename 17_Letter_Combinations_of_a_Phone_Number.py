# 17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str):
        if len(digits)==0:
            return []
        
        result = [""]
        
        digit_map = {
            0: "0",
            1: "1",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        
        for digit in digits:
            n = []
            for char in digit_map[int(digit)]:
                for str in result:
                    n.append(str+char)
            result = n
        return result
            

S = Solution()
y = S.letterCombinations('234')
print(y)
