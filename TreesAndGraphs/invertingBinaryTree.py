"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
#     def invertTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
    def invertTree(self, root):
        # if None, we want to just return None
        if not root:
            return None;
        # get the most recursive right node
        right = self.invertTree(root.right);
        # get the most recursive left node
        left = self.invertTree(root.left);
        # swap the two positions 
        root.left = right
        root.right = left;
            
        return root;        

