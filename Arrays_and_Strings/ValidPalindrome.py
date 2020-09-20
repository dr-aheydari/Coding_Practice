"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.

""" 

class Solution(object):
    def __init__(self):
        # not using any libraries
        self.puncs = [" ", "!","#","$","%","&", "(",")","*","+",
                      ",","-",".","/",":",";","<","=",">","?","@",
                      "[","\\","]","^","_","`","{", "|", "}", "~",
                      "\"","\'"];
        
        # we could alternatively import the string class and use 
        ## string.punctutations 
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.string = self.CleanUp(s);
        return self.string == self.ReverseString()   
    
    def ReverseString(self):
        return self.string[::-1]; 
    
    def CleanUp(self,s):
        # make the string lower 
        string = s.lower();
        for i in self.puncs:
            string = string.replace(i, "")
       
        return string
    
"""
inst = Solution();
s = "Marge, let's \"[went].\" I await {news} telegram.";
# s = "race a car"
print(inst.isPalindrome(s));
"""
