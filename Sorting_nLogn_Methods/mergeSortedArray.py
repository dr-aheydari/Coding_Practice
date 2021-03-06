"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        array1 = nums1[:m];
        i = 0; j = 0; k = 0;
        while i < m  and j < n:
            if array1[i] < nums2[j]:
                nums1[k] = array1[i];
                i+=1;
            else:
                nums1[k] = nums2[j];
                j+=1;
            k+=1;
            
        # if there are any leftover elements from each array 
        while i < m:
            nums1[k] = array1[i];
            i+=1;
            k+=1;
        while j < n:
            nums1[k] = nums2[j];
            j+=1;
            k+=1;
        
