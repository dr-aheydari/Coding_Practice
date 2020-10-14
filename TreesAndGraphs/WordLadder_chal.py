"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""

from collections import defaultdict, deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # if we have an empty string
        if len(beginWord) == 0 or len(endWord) == 0 or endWord not in wordList:
            return 0;
        
        combo_dict = self.Preprocess(wordList, len(beginWord));
        
        # make a queue with the beginning word and its level
        queue = collections.deque([(beginWord, 1)])
        
        # make a dictionary to avoid looking at the same word multiple times
        visited_dict = {beginWord:1};
        
        while queue:
            curr_word, curr_level = queue.popleft();
            for i in range(len(beginWord)):
                possible_combos = curr_word[:i] + "?" +curr_word[i+1:];
                
                # now let's check all the other words that have the same combo possibilites
                for item in combo_dict[possible_combos]:
                    if item == endWord:
                        return curr_level + 1;
                    
                    if item not in visited_dict:
                        visited_dict[item] = 1;
                        queue.append([item,curr_level + 1])
                combo_dict[possible_combos] = [];
        
        # if there is nothing to be done
        return 0;
        
    def Preprocess(self, wordList, length):
        all_combos = defaultdict(list)
        for word in wordList:
            for i in range(length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combos[word[:i] + "?" + word[i+1:]].append(word);
                
        return all_combos;
