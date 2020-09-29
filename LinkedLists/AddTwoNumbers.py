#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # question says non-empty, so I will not do the checks         
        counter1 = 1;
        counter2 = 1;        
        running_num1 = 0;
        running_num2 = 0;
        
        while l1 is not None:
             # this way we get the right positioning
            running_num1 += l1.val * (counter1);
            counter1 *= 10;
            l1 = l1.next;
        
        while l2 is not None:
            # this way we get the right positioning
            running_num2 += l2.val * (counter2);
            counter2 *= 10;
            l2 = l2.next;
            
        # now to get the sum of the two:
        sum_both = running_num1 + running_num2;
        # now get the individual digits
        back_dig = [int(d) for d in str(sum_both)];
        #flip the array
        back_dig  = back_dig[::-1];
        node_list = [ListNode(d) for d in back_dig];
        
        i = 0;
        for node in node_list:
            i+=1;
            if i < len(node_list):
                node.next= node_list[i];
            else:
                node.next = None;
                
        return node_list[0];
        
        
        
    
    def Print(self):
        temp = self;
        while temp is not None:
            print (temp.val)
            temp = temp.next;
            
        print("Null")


first = ListNode(1);
second = ListNode(2);
third = ListNode(3);

first_2 = ListNode(4);
second_2 = ListNode(5);
third_2 = ListNode(6);

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


first.addTwoNumbers(first,first_2).Print()


