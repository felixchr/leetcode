from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        ret = []
        if root.left:
            ret.extend(self.inorderTraversal(root.left))
        ret.append(root.val)
        if root.right:
            ret.extend(self.inorderTraversal(root.right))
        return ret

