#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?


Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def Print(self):
        temp = self;
        while temp is not None:
            print (temp.val)
            temp = temp.next;
            
        print("Null")

# going through the entire list approach
def hasCycle(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # edge case where we have an empty list
        if head == None:
            return False;
        counter = 0;
        while head.next is not None and counter <=10**4:
            counter+=1;
            head = head.next;
        
        print(counter)
        if counter > 10**4:
            return True;
        else:
            return False;
        
## doing two pointers
# def hasCycle_efficient(head):
#         if not head or not head.next: 
#             return False        
        
#         first, second = head, head.next
#         while first != second:
#             if not first or not first.next: return False
#             first, second = first.next, second.next.next
#         return True

        
        
        
first = ListNode(1);
first.next = first;


print(hasCycle(first));

