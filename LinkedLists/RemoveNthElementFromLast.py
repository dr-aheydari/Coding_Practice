"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodes_list = [];
        # traverse the entire linked list
        while head is not None:
            nodes_list.append(head.val);
            head = head.next;
        
        # pop the nth element from the end 
        nodes_list.pop(len(nodes_list) - n);
        
        pre_head = ListNode();
        try:
            new_head = ListNode(nodes_list[0]);
            pre_head.next = new_head;
            for i in range(1,len(nodes_list)):
                new_head.next = ListNode(nodes_list[i]);
                new_head = new_head.next;
            return pre_head.next;
        except:
            return None
        

