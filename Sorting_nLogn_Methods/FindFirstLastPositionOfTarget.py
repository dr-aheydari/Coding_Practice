"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?


Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = 0; j = len(nums) - 1;
        
        # since we have a sorted array, we can take care of edge cases easily:
        if len(nums) == 0 or nums[i] > target: 
            return [-1,-1];
        
        if nums[j] < target:
            return [-1,-1];
        
        # if the array is at least in range:
        ## we want to have a unique set of first and last positions
        ind = set();
        counter = 0;
        # very simple if statements 
        while counter < len(nums):
            if nums[i] < target:
                i+=1;
            if nums[j] > target:
                j-=1;
            if nums[i] == target:
                ind.add(i)
            if nums[j] == target:
                ind.add(j);
            if len(list(ind)) == 2:
                return sorted(list(ind))
            counter+=1;
        
        # in case if we had only one position
        if len(list(ind)) == 1:
            return [list(ind)[0],list(ind)[0]]
            
        return [-1,-1];

