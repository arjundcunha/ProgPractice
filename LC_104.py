# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getdepth(self, node, depth):
        if node == None:
            return 0
        depth += 1
        le = 0
        ri = 0
        if node.left != None:
            le = self.getdepth(node.left, depth)
        if node.right != None:
            ri = self.getdepth(node.right, depth)
        
        return max(depth, max(le,ri))
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = self.getdepth(root,0)
        return depth
        