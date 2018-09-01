class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for x in strs:
            y = x
            curr = ''.join(sorted(x))
            if ans.has_key(curr):
                ans[curr].append(str(y))
            else:
                ans[curr] = [str(y)]
        # finalans = []
        # for x in ans.keys():
        #     finalans.append(ans[x])
        return ans.values()
        