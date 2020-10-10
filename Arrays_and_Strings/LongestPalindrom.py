"""



"""

class Solution:
    def longestPalindrome(self, s):
        # substring to store palindrome
        sub = ''; 
        for i in range(len(s)):
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(sub) >= j-i:  # To reduce time
                    break;
                elif s[i:j] == s[i:j][::-1]:
                    sub = s[i:j];
                    break
        return sub

