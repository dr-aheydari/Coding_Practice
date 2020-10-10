"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'

"""

class Solution(object):
    
    def isValid(self, s):
        # a map for looking up 
        my_map = {"(": ")", "[": "]",  "{": "}"}
        left = ["(", "[", "{"]
        my_stack = []
        for i in s:
            if i in left:
                my_stack.append(i)
            # look up if the correpsonding right bracket is in the array 
            elif my_stack and i == my_map[my_stack[-1]]:
                    # if yes, remove the left one
                    my_stack.pop()
            else:
                return False
            
        return my_stack == []


