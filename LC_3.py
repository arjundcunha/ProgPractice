class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        x = 0
        curr_ma = 0
        curr_l = 0
        cu_s = set()
        while x<len(s):
            if s[x] in cu_s:
                curr_ma = max(curr_l, curr_ma)
                curr_l = x - dic[s[x]]
                cu_s = set(s[dic[s[x]]+1:x+1])
                dic[s[x]] = x
            else :
                curr_l += 1
                cu_s.add(s[x])
                dic[s[x]] = x
            x += 1
        return (max(curr_ma, curr_l))
                
        