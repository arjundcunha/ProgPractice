class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        array = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                array.append(x)
            else:
                if len(array) == 0:
                    return False
                if x == ')' and array[len(array)-1] == '(':
                    array = array[:len(array)-1]
                elif x == ']' and array[len(array)-1] == '[':
                    array = array[:len(array)-1]
                elif x == '}' and array[len(array)-1] == '{':
                    array = array[:len(array)-1]
                else:
                    return False
        if len(array) == 0:
            return True
        else:
            return False
                    
        