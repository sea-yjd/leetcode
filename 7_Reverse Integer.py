class Solution:
    def reverse(self, x: int):
        ## 判断区间大小
        if not (-math.pow(2,31) + 1 < x < math.pow(2,31)):
            return 0
        p = 1
        new = ''
        ## 判断正负
        if x < 0:
            p = -1
            x = p * x
        string = str(x)
        new = string[::-1]
        # i = len(string) - 1
        # while i >= 0:
        #     new += string[i]
        #     i -= 1
        new = int(new) * p
        if not (-math.pow(2,31) + 1 < new < math.pow(2,31)):
            return 0
        return new
      
      """
      solution2:
      num = 0
        a= abs(x)
        while(a!=0):
            temp = a % 10
            a = int(a/10)
            num = num*10 + temp
            
        if x>0 and num <2147483647:
            return num
        elif x<0 and num<=2147483647:
            return -num
        else:
            return 0
      """
      
S = Solution()
y = S.reverse(x = 1534236469)
print(y)
