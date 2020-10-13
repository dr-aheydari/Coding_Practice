
"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
The number of nodes will not exceed 1000.


"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old
        
        
        
        
##### TO RETURN AS A LIST NOT NODES : )      
# class Solution(object):
#     def copyRandomList(self, head):
#         """
#         :type head: Node
#         :rtype: Node
#         """
#         # if empty return None
#         if not head:
#             return None;
        
#         original_head = head;
        
#         node_dict = {};
#         counter = 0;
#         node_vals = [];
        
#         while head is not None:
#             node_dict[head.val] = counter;
#             node_vals.append(head.val)
#             head = head.next;
#             counter +=1;
        
#         print(node_dict)
#         deep_copy = [];
#         iterator = 0;
#         while original_head is not None:
#             try:
#                 rand_val = original_head.random.val;
#                 print(rand_val);
#                 # if the random node is pointing to something
#                 rand_index = node_dict[rand_val];
#                 print(rand_index)
#                 deep_copy.append([node_vals[iterator],rand_index])
#             except:
#                 # if it is pointing to None
#                 deep_copy.append([node_vals[iterator],None])

#             iterator +=1;
#             original_head = original_head.next;
            
#         print(deep_copy)
#         return deep_copy;
                

