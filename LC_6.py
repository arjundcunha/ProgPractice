class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = ['']*numRows
        flag = True
        y = 0
        for x in range(len(s)):
            if flag:
                curr = y
                ans[curr] += s[x]
                y += 1
                if (y)%numRows == 0:
                    flag = False
                    y = 2
            else:
                curr = numRows - y
                ans[curr] += s[x]
                y += 1
                if y%numRows == 0:
                    flag = True
                    y = 0
        finalans = ''
        for x in ans:
            finalans += x
        return finalans