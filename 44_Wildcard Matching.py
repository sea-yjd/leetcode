class Solution:
    restore = dict()
    def removeDulicatedStar(self, p):
        if p == '': return p
        new = [p[0]]
        for i in range(1,len(p)):
            if p[i] == '*' and p[i-1] == '*':
                continue
            new.append(p[i])
        return ''.join(new)
    def help(self, s, p):
        if (s,p) in self.restore: return self.restore.get((s,p))
        if p == '*':
            return True
        if s == '' :
            return not p
        if p == '':
            return not s
        len_s = len(s)
        len_p = len(p)
        for i in range(len_s):
            for j in range(len_p):
                if s[i] == p[j] or p[j] == '?':
                    ans = self.help(s[1:],p[1:])
                    self.restore[(s,p)] = ans
                    return ans
                elif p[j] == '*':
                    ans = self.help(s[1:],p) or self.help(s,p[1:])
                    self.restore[(s,p)] = ans
                    return ans
                return False
    def isMatch(self, s: str, p: str) -> bool:
        return self.help(s,self.removeDulicatedStar(p))
S = Solution()
y = S.isMatch('acdcb','a*c?b')
print(y)
