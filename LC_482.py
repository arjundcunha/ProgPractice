def reverse(st):
    toret = ""
    for x in st:
        toret = x + toret
    return toret

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        tot = ''
        for x in S:
            if x != '-':
                if x.isalpha():
                    tot = x.upper() + tot
                else:
                    tot = x + tot
        ans = ''
        for x in range(0,len(tot), K):
            ans =  reverse(tot[x:x+K]) + '-' + ans
        return ans[:-1]