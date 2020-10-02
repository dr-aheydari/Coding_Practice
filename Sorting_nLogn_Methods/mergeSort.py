#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Merge Sort code:
    time complexity: O(nlog(n))
    space complexity: O(n) -> since we store an auxiliry array 
    
"""

class MergeSort():
    
        
    def mergeSort(self,array):
        
        if len(array) > 1:
            middle = int(len(array)/2);
            # split the array to left and right up to the middle point
            left_array = array[:middle];
            right_array = array[middle:];
            
            self.mergeSort(left_array);
            self.mergeSort(right_array);
            
            # merge the lists 
            
            i = 0; j = 0; k = 0;
            while i<len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    array[k] = left_array[i];
                    i+=1;
                else:
                    array[k] = right_array[j];
                    j+=1;
                    
                k+=1;
               
               # now let's see if there are any left overs that we did not consider
               
            while i < len(left_array):
                   array[k] = left_array[i];
                   i+=1;
                   k+=1;
                   
            while j < len(right_array):
                  array[k] = right_array[j];
                  k+=1;
                  j+=1;
                  
        return array;
        

    def Print(self, arr): 
        for i in range(len(arr)):         
            print(arr[i], end =" ") 
        print();
            

obj = MergeSort();

arr = [7, 12, 15, 0, 8, 13, 15, 8, 22, 2]  
print ("Given array is", end ="\n")  
obj.Print(arr);
sorted_arr = obj.mergeSort(arr)
print("Sorted array is: ", end ="\n") 
obj.Print(sorted_arr);

