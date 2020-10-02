"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]

"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = 10;
        iter_lim = 0;
        i = 0;
        my_dict = {};
        return_list = [];
        if len(s) == length + 1:
            iter_lim = len(s)+1
        else:
            iter_lim = len(s)
            
        while i + length < iter_lim:
            
            if str(s[i:i+length]) in my_dict.values() and i > 0:
                if s[i:i+length] in return_list:
                    return return_list;
                else:
                    return_list.append(s[i:i+length])
            else:
                 my_dict[i] = s[i:i+length];
            i+=1;
              
        return return_list;


