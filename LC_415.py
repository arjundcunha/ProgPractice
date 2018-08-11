def reverse(s):
    st = ""
    for i in s:
        st = i + st
    return st
 
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = reverse(num1)
        num2 = reverse(num2)
        total = max(len(num1), len(num2))
        ans = ''
        carry = 0
        for x in range(total):
            if x >= len(num1):
                curr = carry + int(num2[x])
            elif x>= len(num2):
                curr = carry + int(num1[x])
            else:
                curr = carry + int(num1[x]) + int(num2[x])
            
            carry = int(curr / 10)
            ans += str(curr%10)
        if carry>0:
            ans += str(carry)
        return (reverse(ans))
                
        
        