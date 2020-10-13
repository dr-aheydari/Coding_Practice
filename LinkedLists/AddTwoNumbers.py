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
        running_sum = 0;
        tens = 1;
        while l1 is not None and l2 is not None:
            running_sum += (l1.val + l2.val)*tens;
            tens *=10;
            l1 = l1.next; l2 = l2.next;
        
        # only one of these cases will be true!
        
        while l1 is not None:
            running_sum += l1.val * tens;
            tens *=10;
            l1 = l1.next;
        
        while l2 is not None:
            running_sum+= l2.val * tens;
            tens *=10;
            l2 = l2.next;
        
        # now here make it a linked list
        iter_num = str(running_sum);
        iter_num = iter_num[::-1];
        new_head = ListNode();
        new_next = ListNode(iter_num[0]);
        new_head.next = new_next;
        for i in range(1,len(iter_num)):
            new_next.next = ListNode(int(iter_num[i]));
            new_next = new_next.next;
        
        
        return new_head.next;
    
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


