# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_same(left_tree_root, right_tree_root):
            if not left_tree_root and not right_tree_root:
                return True
            if not left_tree_root or not right_tree_root or left_tree_root.val != right_tree_root.val:
                return False
            
            is_left_subtree_same = is_same(left_tree_root.left, right_tree_root.left)
            is_right_subtree_same = is_same(left_tree_root.right, right_tree_root.right)

            return is_left_subtree_same and is_right_subtree_same
        return is_same(p, q)
            