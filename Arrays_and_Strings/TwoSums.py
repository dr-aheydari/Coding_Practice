"""
Question:
    
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


"""


class Solution(object):
# brute force solution,
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(0,len(nums)):
#             for j in range(i,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     # whenever we find these numbers, we can return them 
#                     return [i,j]
                
#         # if there are not such numbers in the list
#         return [None,None]
    
        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            self.list = nums;
            self.target = target;
            self.dict = self.list2Dict(self.list);
            for i in range(0,len(self.list)):    
                j = self.getIndex(i);
                if j == i or j == None:
                    continue;
                # one last check to make sure all is good 
                print(self.list[i] + self.list[j]);
                if self.list[i] + self.list[j] == target:
                    return [i,j];
            
            
        def list2Dict(self, inp_list):
             return {i:inp_list[i] for i in range(0,len(inp_list))}    
    
        def getIndex(self,curr_index):
            needed_val = self.target - self.list[curr_index]
            try:
                return list(self.dict.keys())[list(self.dict.values()).index(needed_val)]  
            except:
                return None
        


"""
# testing         

inst = Solution();
nums = [3,2,3];
target = 6;
answer = inst.twoSum(nums, target)

print(answer);

"""

