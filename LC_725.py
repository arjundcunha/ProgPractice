# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getlength(node):
    curr = 0
    while (node != None):
        curr += 1
        node = node.next
    return curr

def makelit(curr, size):
    head = curr
    for x in range(0,size):
        temp = curr
        curr = curr.next
    temp.next = None
    return head,curr
    

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        head = root
        curr = root
        leng = getlength(root)
        ans = []
        if leng == 0:
            return [root]*k
        elif leng<=k:
            while curr != None:
                ans.append(ListNode(curr.val))
                curr = curr.next
            while leng != k:
                ans.append(None)
                leng += 1
        else:
            extra = leng%k
            num = int(leng/k)
            for _ in range(0,extra):
                toadd, curr = makelit(curr,num+1)
                ans.append(toadd)
            
            left = k-extra
            for _ in range(0,left):    
                toadd, curr = makelit(curr,num)
                ans.append(toadd)
                
        return ans
        