# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root is None:
                return (True, -1)
            
            left_ok, left_h = check(root.left)
            right_ok, right_h = check(root.right)

            balanced = left_ok and right_ok and abs(left_h - right_h) <= 1

            return (balanced, max(left_h,right_h) + 1)
        balanced,_ = check(root)
        return balanced 
        