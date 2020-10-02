"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # we have two pointer traversing the array, so we get a linear time complexity 
        # as we go through the array, I will keep track of the complement of each value
        my_dict = {};
        i = 0; j = 0;
        # i is the low, j is the high
        while j < len(nums):
            difference = target - nums[j];
            my_dict[j] = difference;
            if nums[j] in my_dict.values():
                index = list(my_dict.keys())[list(my_dict.values()).index(nums[j])];
                if j != index:
                    return[j,index]
            j+=1;


