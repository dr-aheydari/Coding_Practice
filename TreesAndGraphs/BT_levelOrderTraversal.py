"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    
    def levelOrder(self, node):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # if we get to null, we should return
        outer_list = [];
        
        if not node:
            return outer_list;
        
        def Recursion(node, inner_level):
            
            if node:
                if len(outer_list) == inner_level:
                    outer_list.append([])    
                    
                outer_list[inner_level] += [node.val];
                Recursion(node.left,inner_level+1);
                Recursion(node.right, inner_level+1);
                    
        Recursion(node,0);
        return outer_list;
    

