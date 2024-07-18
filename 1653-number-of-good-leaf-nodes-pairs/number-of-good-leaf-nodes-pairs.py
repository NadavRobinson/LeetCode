# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0
        def rec(root):
            nonlocal count
            if not root: return []
            if not root.left and not root.right:
                return [0]
            arrL = rec(root.left)
            arrR = rec(root.right)
            for d1 in arrL:
                for d2 in arrR:
                    if d1 + d2 + 2 <= distance:
                        count += 1
            return [a + 1 for a in (arrR + arrL)]
        rec(root)
        return count
    


        