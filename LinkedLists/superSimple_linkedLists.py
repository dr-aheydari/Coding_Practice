## Linked List


class Node():
    
    def __init__(self,value = None):
        self.value = value;
        self.next = None; #initialize to null
        
class LinkedList():
    def __init__(self):
        self.head = None; # initialize to null

#### printing the elements in the list 
        
    def Print(self):
        printval = self.head
        while printval is not None:
            print (printval.value)
            printval = printval.next;
            
#### adding elements to the first
    def InsertFirst(self, head_value):
        new_head = Node(head_value);
        new_head.next = self.head;
        self.head = new_head;
        
#### adding elements to the last
    def InsertLast(self, head_value):
        new_last = Node(head_value);
        # to check if we have no other elements in the list
        if self.head == None:
            self.head = new_last;
            return;
        
        iter_element = self.head;
        # since we do not care if the values are None or not
        while (iter_element.next):
            iter_element = iter_element.next;
        
        # finally link the last existing val to the new end element
        iter_element.next = new_last;
        
#### adding elements in between to links
    def InsertMiddle(self,new_middle ,lvalue, rvalue):
        middle = Node (new_middle)
        lvalue.next = middle;
        middle.next = rvalue;
        
            
ll = LinkedList();
first = Node("this")
second = Node("is")
third = Node("a")
fourth = Node("Linked");
fifth = Node("List");

# set the head node
ll.head = first;
# link the head to the second value
ll.head.next = second;
second.next = third;
third.next = fourth;
fourth.next = fifth;

ll.InsertFirst("no_way");
ll.InsertLast("last");
ll.InsertMiddle("middle", first, second);

ll.Print();

