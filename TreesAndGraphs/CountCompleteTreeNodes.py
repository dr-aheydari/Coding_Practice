"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0;
        
        self.count = 0;
        count = self.Traverse(root);
        
        return count;
        
        
    def Traverse(self, root):
        # we do this as an pre-order traversal
        if not root:
            return None;
        
        print(root.val);
        self.count +=1;
        self.Traverse(root.left);
        self.Traverse(root.right);
        
        return self.count;
