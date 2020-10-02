class QuickSort():
    
    def quickSort(self, array, low, high):
        if low < high:
            #we recursively keep calling the partition function
            part_index = self.partition(array,low,high);
            # seperately sort elements before and after partitioning
            self.quickSort(array,low,part_index - 1);
            self.quickSort(array,part_index + 1,high);
            
                return array;

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

### testing
# Driver code to test above
obj = QuickSort();
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print ("original array is:")
for i in range(n):
    print(f"{arr[i]}",end=" ")
print();

sorted_array = obj.quickSort(arr,0,n-1);
print ("Sorted array is:")
for i in range(n):
    print(f"{arr[i]}",end=" ") 
