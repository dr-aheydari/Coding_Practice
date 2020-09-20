"""
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.

"""

class Solution(object):
    
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.list = self.ExtractWords(s);
        
        floor_len = int(len(self.list)/2)
        for i in range(0,floor_len):
            self.Swap(i,(-1-i));
            
        return ' '.join(self.list)
        
    def Swap(self, i, j):
        temp = self.list[i];
        self.list[i] = self.list[j];
        self.list[j] = temp;
        
        
    def ExtractWords(self, string):
        # removeing left and white spaces from the string
        string = string.strip();
        return string.split()
        
