"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up:

Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
		self.return_array = [];
    
    def inorderTraversal(self,node):
		# we want to visit the left subtree first, print all the values and then root, then right
		
		#if we have node to be null
		if not node:
			return None;

		# let's get to the most left subtree	
		self.inorderTraversal(node.left);
		
		self.return_array.append(node.val);
		
		# now lets do the same for the right subtrees 
		self.inorderTraversal(node.right);
        
		return self.return_array;
        
        
        






