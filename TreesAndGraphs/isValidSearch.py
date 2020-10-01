"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
#     def isValidBST(self,root):
#         # an empty tree is passed
#         if root == None:
#             return True;
#         # a tree with only the root 
#         if not root.right and not root.left:
#             return True;

#         return self.RecursiveCheck(root);
    
    
#     def RecursiveCheck(self, node, flag=None):
        
#         if not node:
#             return True;
        
#         if not flag:
#             self.prev_largest_r = node.val;
#             self.prev_smallest_l = node.val;
        
#         if flag == 'r':
#             if self.prev_largest_r >= node.val:
#                 return False
#             else:
#                 self.prev_largest_r = node.val;
                
#         if flag == 'l':
#             if self.prev_smallest_l <= node.val:
#                 return False;
#             else:
#                 self.prev_smallest_l = node.val;
        
#         print(self.prev_largest_r)
#         print(self.prev_smallest_l)
#         print("------------------")
        
#         if node.left and node.left.val >= node.val:
#             return False;
        
#         if node.right and node.right.val <= node.val:
#             return False
        
#         return self.RecursiveCheck(node.left,'l') and self.RecursiveCheck(node.right,'r')

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
    




