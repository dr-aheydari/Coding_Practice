#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

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

def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ## Question says that there will not be an empty node as input
        counter1 = 1;
        counter2 = 1;
        running_list1 = [];
        running_list2 = [];
        
        while l1 is not None:
            running_list1.append(l1.val);
            l1 = l1.next;
            counter1*=10;
            
        while l2 is not None:
            running_list2.append(l2.val);
            l2 = l2.next;
            counter2*=10;
        
        # these are going to be for the running numbers 
        run_num1=0;
        run_num2=0;
        
        # get the numbers in order
        for i in running_list1:
            counter1 /= 10;
            run_num1 += i * counter1;
        print(run_num1)
        
        for i in running_list2:
            counter2 /= 10;
            run_num2 += i * counter2;
            
        print(run_num2)
        sum_both = run_num1 + run_num2;
        
        # now make a linkedList for the new digits
        digs = [ListNode(int(d)) for d in str(int(sum_both))];
        # turn them into a linkedList
        q = 0;
        for node in digs:
            q +=1;
            if q < len(digs):
                node.next = digs[q];
            else:
                node.next = None;
        
        return digs[0];
        
    
### testing 
        
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

addTwoNumbers(first,first_2).Print();
  
