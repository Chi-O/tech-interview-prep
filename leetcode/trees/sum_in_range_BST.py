"""
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].
Leetcode #938
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root:
            if root.val < low:
                return self.rangeSumBST(root.right)
            elif root.val > high:
                return self.rangeSumBST(root.left)
            else:
                return root.val + self.rangeSumBST(root.right) + self.rangeSumBST(root.left)
        else:
            return 0
        
