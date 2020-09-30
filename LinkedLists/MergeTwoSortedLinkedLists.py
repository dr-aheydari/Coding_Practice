#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

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
        
def mergeTwoLists(l1, l2):
        
    """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
    """
    #######################
    # edge cases when we have either one or both empty 
    if l1 is None and l2 is not None:
        return l2;
        
    if l1 is not None and l2 is None: 
        return l1;
    
    if l1 is None and l2 is None:
        return None;
    #######################
    
    # get a reference to the node before head
    head_m1 = ListNode(-1);

    last_iter = head_m1
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            last_iter.next = l1
            l1 = l1.next
        else:
            last_iter.next = l2
            l2 = l2.next            
        last_iter = last_iter.next

    # so now if we have either one of the lists to be null, just append
    last_iter.next = l1 if l1 is not None else l2

    return head_m1.next
                
    
    
first = ListNode(1);
second = ListNode(2);
third = ListNode(4);

first_2 = ListNode(0);
second_2 = ListNode(3);
third_2 = ListNode(5);

items = [first, second, third]
items2 =[first_2, second_2, third_2]

i = 0;
for item in items:
    i+=1;
    if i < len(items):
        item.next = items[i];
    else:
        item.next = None;
        break;
i = 0;
for item in items2:
    i+=1;
    if i < len(items2):
        item.next = items2[i];
    else:
        item.next = None;
        break;



first.Print();
first_2.Print();

print("Solution:")

mergeTwoLists(first,first_2).Print();


