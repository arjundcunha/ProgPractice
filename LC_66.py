class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        le = len(digits)-1
        carry = 1
        if digits[le] != 9:
            digits[le] += 1
        else:
            while(True):
                if carry == 0 or le == -1:
                    break
                else:
                    digits[le] += 1
                    carry = digits[le]/10
                    digits[le] = digits[le]%10
                    le -= 1
            if carry != 0:
                digits = [1] + digits
        return digits
                    
        