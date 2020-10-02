"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.

"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # if we wanted to use the std library 
        ## nums.sort()
        
#         # approach (1) Merge Sort: Complexity -> O(n) in space, O(nLog(n)) in time 
#         if len(nums) > 1:
#             middle = int(len(nums)/2); # or we could say len(nums)//2

#             left_array = nums[:middle];
#             right_array = nums[middle:];

#             self.sortColors(left_array);
#             self.sortColors(right_array);

#             i = 0; j = 0; k = 0;
#             while i < len(left_array) and j < len(right_array):
#                 if left_array[i] < right_array[j]:
#                     nums[k] = left_array[i];
#                     i+=1;
#                 else:
#                     nums[k] = right_array[j];
#                     j+=1;
#                 k+=1;

#             while i < len(left_array):
#                 nums[k] = left_array[i];
#                 i+=1;
#                 k+=1;
#             while j < len(right_array):
#                 nums[k] = right_array[j];
#                 j+=1;
#                 k+=1;

#         

# approach (2) Quick Sort: Complexity -> O(1) in space, O(nLog(n)) in time on avg 
        self.quickSort(nums, 0, len(nums)-1);
    
    def quickSort(self, array, low, high):  
        if low < high:
            #we recursively keep calling the partition function
            part_index = self.partition(array,low,high);
            # seperately sort elements before and after partitioning 
            self.quickSort(array,low,part_index - 1);
            self.quickSort(array,part_index + 1,high);

    def partition(self, array, low, high):
        # index of the smaller element
        i = (low-1);
        # chose the pivot element
        pivot = array[high];
        for q in range(low,high):
            if array[q] < pivot:
                i+=1;
                # swap the positions to get the right place for the pivot
                array[i],array[q] = array[q],array[i];
            
        array[i+1],array[high] = array[high],array[i+1];
        return (i+1)

