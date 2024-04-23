# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node, p, q):
        # base case, we've found either p or q (so return one of them), or it's None (so return None)
        if not node or p == node or q == node:
            return node

		# recursively check both sides of the children of this current node
        left  = self.lowestCommonAncestor( node.left, p, q)
        right = self.lowestCommonAncestor(node.right, p, q)

		# if we found BOTH p and q, we're done! return this node, it's the LCA
        if left and right:
            return node

		# otherwise, return "left" or "right". This will either return: None, P, or Q
        return left or right
        
