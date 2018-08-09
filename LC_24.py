# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        keep = head.next    #2
        head.next = head.next.next #1 3
        keep.next = head # 2 1 3
        # 2 1 3 4
        one = keep.next # 1
        two = one.next  # 3
        while two != None and two.next != None:
            one.next = two.next # 2 1->4
            two.next = two.next.next # 3->5
            one.next.next = two # 2143
            one = two
            two = one.next
        return keep
            
        