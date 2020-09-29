'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
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

def reverseList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head;
        # temp is first
        counter = 0;
        flag = 'Y';
        while current is not None and flag != 'N':
            # store the current element
            # print(f"Current: {current.val}");
            first = current; 
            if counter == 0:
                try:
                    # find the next element
                    second = current.next;
                    current.next = None;
                    current = second.next;
                    if current == None:
                        # this means we are in an edge case so we want to exit
                        head = second;
                        second.next = first;
                        return head;
                        
                    second.next = first;
                    next_element = second;
                except:
                    # this means we are in an edge case so we want to exit
                    flag='N';
            else:
                try:
                    next_iter = current.next;
                    current.next = next_element;
                    current = next_iter;
                    next_element = first;
                    head = first;
                except:
                    # this means we are in an edge case so we want to exit
                    flag = 'N';
            counter+=1;
            
        return head;
        

## test case 1

# first = ListNode(1);
# second = ListNode(2);
# third = ListNode(3);
# fourth = ListNode(4);
# fifth = ListNode(5);
# sixth = ListNode(6);

# items = [first, second, third, fourth, fifth, sixth];
# i = 0;
# for item in items:
#     i+=1;
#     if i < len(items):
#         item.next = items[i];
#     else:
#         item.next = None;
#         break;

## test case 2           
## -> edge case 1
first = ListNode(1);
second = ListNode(2);

items = [first, second];
i = 0;
for item in items:
    i+=1;
    if i < len(items):
        item.next = items[i];
    else:
        item.next = None;
        break;
             
## test case 3           
## -> edge case 2
first = ListNode(1);

items = [first];
i = 0;
for item in items:
    i+=1;
    if i < len(items):
        item.next = items[i];
    else:
        item.next = None;
        break;
                   
        
        
## printing for verification
print("Original")
first.Print();
print(" ")
print(" ")
head = reverseList(first);
print("Reversed")
head.Print();

