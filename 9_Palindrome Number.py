## 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        # Solution1:
        # string = str(x)
        # string_p = string[::-1]
        # if string == string_p:
        #     return True
        # else:
        #     return False

        # Solution2:
        x1 = x
        s = 0
        while (x):
            temp = x % 10
            x = int(x/10)
            s = s * 10 + temp

        if s == x1:
            return True
        else:
            return False
S = Solution()
y = S.isPalindrome(121)
print(y)
