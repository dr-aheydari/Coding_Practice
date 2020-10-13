"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

 
Example 1:

Input: root = [1,2,3]
Output: 6
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
 

Constraints:

The number of nodes in the tree is in the range [0, 3 * 104].
-1000 <= Node.val <= 1000

"""

class Solution(object):
    def __init__(self):
        self.sums = [];
        self.all = []
        self.running_sums = 0;
        self.nodes = [];

    def maxPathSum(self, root):
        # I want to traverse every possible path, and then store the value of that path in an array     which I can take the max of later

        # if the root is None
        if not root:
            return None;
        
        while root is not None:
            self.Traverse(root);
            temp = sum(self.sums);
            self.sums = [];
            self.all.append(temp);
            try:
                root = root.right;
            except:
                root = None;
                
        # check to see if there is any individual node that has the highest value 
        ## if yes, then that by itself would be the path 
        
        return max(max(self.all),max(self.nodes))
        
    def Traverse(self, root):
        
        # I want to do in order traversal
        if not root:
            return root;
        # saving all the nodes that we've visited 
        self.nodes.append(root.val);
        # add the current value to the running sums 
        self.running_sums += root.val;
        # recursively traverse the tree
        self.Traverse(root.left);
        self.Traverse(root.right);
        # add the current traverse to the a running array of sums
        self.sums.append(self.running_sums);
        # reset the running sums 
        self.running_sums = 0;


