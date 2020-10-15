"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# recursive solution
class Solution():
	def __init__(self):
		self.outLvl = [];

	def levelOrder(self, root):

		if not root:
			return;
		# make a call to BFS_Traverse function
		self.BFS_Traverse(root,0);

		return self.outLvl;
		
	def BFS_Traverse(self, root, counter):
		# create an array inside the list for each lvl
		if len(self.outLvl) == counter:
			self.outLvl.append([]);

		# now add the value of the root to the list
		self.outLvl[counter] += [root.val];
		# do this recursively
		for child in root.children: 
			self.BFS_Traverse(child, counter + 1);

