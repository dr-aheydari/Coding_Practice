"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
Example 3:

Input: matrix = [], target = 0
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100

"""

import numpy as np

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.target = target;
        self.search_result = False;
        oneD = np.array(matrix).flatten();
        self.DandC(oneD);
        return self.search_result;
        
    # my divide and conquer approach 
    def DandC(self, oneD):
        if len(oneD) > 1:
            middle = int(len(oneD)/2);
            print(middle)
            if oneD[middle] > self.target:
                self.DandC(oneD[:middle])

            elif oneD[middle] < self.target:
                self.DandC(oneD[middle:])

            elif oneD[middle] == self.target:
                self.search_result = True;
            else:
                self.search_result = False;
                return;
        else:
            if oneD == self.target:
                self.search_result = True;
            else:
                return;
        
        
#         ## Brute Force Solution
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if matrix[i][j] == target:
#                     return True;
