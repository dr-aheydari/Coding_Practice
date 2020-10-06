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


class Solution(object):

    def searchRange(self, nums, target):
        self.target = target;
        left_index = self.DandC(nums, True)

        if  left_index == len(nums) or nums[ left_index] != self.target:
            return [-1, -1]

        return [left_index, self.DandC(nums, False)-1]
    
    def DandC(self, nums, left):
        low = 0
        high = len(nums)

        while low < high:
            middle = int((low + high)/2)
            
            if nums[middle] > self.target or (left and self.target == nums[middle]):
                high = middle;
            else:
                low = middle + 1

        return low

    
### another incomplete solution
    
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         self.index = None;
#         self.target = target;
#         self.DandC(nums)
        
#         if len(nums) == 1:
#             if nums[0] == target:
#                 return [0 , 0]
#             else:
#                 return [-1,-1]
# #         if len(nums) == 2:
# #             if nums[0] == target and nums[0] != nums[1]:
# #                 return [0 , 0]
# #             elif nums[1] == target and nums[0] != nums[1]:
# #                 return [1 , 1]
# #             elif nums[0] != nums[1]:
# #                 return [-1,-1]
        
#         if self.index is not None and len(nums) > 1:
            
#             if self.index + 1 < len(nums):
#                 if nums[self.index + 1] == target:
#                     return [self.index, self.index + 1]

#             if self.index - 1 >= 0:
#                 if nums[self.index - 1] == target:
#                     return [self.index - 1 , self.index]
            
#             if nums[self.index] == target:
#                 return [self.index , self.index]
#         else:
#             return [-1,-1]
        

#     def DandC(self, array):
        
#         if len(array) > 1:
#             middle = int(len(array)/2);
#             if array[middle] > self.target:
#                 self.DandC(array[:middle]);
#             elif array[middle] < self.target:
#                 self.DandC(array[middle:]);
#             elif array[middle] == self.target:
#                 print("YES!")
#                 self.index = middle;
#             else:
#                 return;
            
#         elif len(array) == 1:
#             if array[0] == self.target:
#                 return 0;
            
