"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def __init__(self):
        self.outer_level = [];
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None;
        
        self.LevelOrder(root, 0);
        
        for level in self.outer_level:
            for j in range(len(level)-1):
                if j== len(level)-1:
                    level[j].next = None;
                else:
                    level[j].next = level[j+1];
        
        return root;
        
    def LevelOrder(self, root, counter):
        # if we don't have a None
        if root:
            if len(self.outer_level) == counter:
                self.outer_level.append([])
            
            self.outer_level[counter] += [root];
            
            self.LevelOrder(root.left,counter + 1);
            self.LevelOrder(root.right,counter + 1);
            

