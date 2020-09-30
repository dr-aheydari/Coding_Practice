#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:33:07 2020

@author: aliheydari
"""

class BstNode:

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.right = right;
        self.left = left;

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)
        
    def naive_Assign(self, pos_list,assign_list):
        
        
        # left child:
        root = BstNode(-1);
        assert len(assign_list) == len(pos_list), "not equl!"
        temp = root;
        
        for i in range(len(assign_list)):
            print(temp.key);
            
            if pos_list[i] == 'l':
                
                temp.left = BstNode(assign_list[i]);
                temp.right = BstNode(None);
                temp = temp.left;
            else : 
                temp.right = BstNode(assign_list[i]);
                temp.left = BstNode(None);
                temp = temp.right;

         
        self.left = root.left;
        self.right = root.right;

    def Larger_Left(self, list):
        root = BstNode(-1);
        temp = root;
        i = 0;
        while i < len(list):
            if i < len(list):
                  temp.left = BstNode(list[i]) if list[i] > list[i+1] else BstNode(list[i+1])
                  temp.right = BstNode(list[i]) if list[i] <= list[i+1] else BstNode(list[i+1])
                  temp = temp.left;
                  i+=2;
            else:
                  temp.left = BstNode(list[i]);
                  temp.right = None;
                  break;

        self.right = root.right;
        self.left = root.left;

    def Larger_Right(self, list):
        root = BstNode(-1);
        temp = root;

        i = 0;
        while i < len(list) + 1:
            print(i)
            if i < len(list)-2:
                  temp.right = BstNode(list[i]) if list[i] > list[i+1] else BstNode(list[i+1])
                  temp.left = BstNode(list[i]) if list[i] <= list[i+1] else BstNode(list[i+1])
                  temp = temp.right;
                  i+=2;
            else:
                  
                  temp.right = None;
                  temp.left = BstNode(list[i]);
                  i+=2;

        self.right = root.right;
        self.left = root.left;





    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2




assign_list = [4,5,6,-1,-2,-3];
pos_list = ['l','l','l','r','r','r','l'];
b = BstNode(50);
# b.naive_Assign(pos_list, assign_list)
b.Larger_Right(assign_list)
print("HERE WE GO")
b.display()



