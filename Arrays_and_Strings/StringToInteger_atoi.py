"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
             
"""


class Solution(object):
    def __init__(self):
        self.sign = "";
        self.str_num = "";
        self.pos_inf = (2**31) - 1;
        self.neg_inf = -(2**31);
        
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        try:        
            # now we proceed
            self.string = self.CleanUp(string);
            # if the first none-white character is not a number
            if self.string == None:
                return 0;
            else:
                self.getDigits(self.string);
                num =int(self.sign + self.str_num);
                return self.bitCheck(num);
        except:
            return 0;
    
    def CleanUp (self,string):
        # strip the white space from the left hand side
        string = string.lstrip()
        try:
            # here we basically have a switch case
            if string[0] == "+":
                # since we want to replace once we add 1 to replace
                return string.replace("+","",1);
            
            elif string[0] == "-":
                # we need the negative sign at the end
                self.sign += "-";
                # since we want to replace once
                return string.replace("-","",1);
                
            elif string[0].isdigit():
                return string;
            else:    
                return None;
        except:
            return 0;
    
    def getDigits(self,string):
        if string == "":
            self.str_num = "0";
            return 0;
        
        for char in string:
            if char.isdigit():
                self.str_num += char;
            else:
                return 0;
            
        
    def bitCheck(self, num):
        # one last check for min and max 32 signed ints
        if num < self.neg_inf:
            return self.neg_inf;
        
        elif num > self.pos_inf:
            return self.pos_inf;
        
        else:
            return num;
        
""" 

inst = Solution();
string = "-4193 with words";
# string = "42"
# string = "words and 987";
# string = "+91283472332";
# string = "-91283472332";
# string = "++1";
print(inst.myAtoi(string));

"""
