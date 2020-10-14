"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""

from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # make a graph 
        table = defaultdict(defaultdict);
        # map the associated division values to the respective variable
        for i in range(len(equations)):
            table[values[i]] = equations[i];
            
        # Step 1). build the graph from the equations
        for (num, denum), val in zip(equations, values):
            # add nodes and two edges into the graph

            table[num][denum] = float(val)
            table[denum][num] = float(1. / val)
            
        # Step 2). Evaluate each query via backtracking (DFS)
        #  by verifying if there exists a path from dividend to divisor
        results = []
        for num, denum in queries:
            if num not in table or denum not in table:
                # case 1): either node does not exist
                ans = -1.0
                
            elif num == denum:
                # case 2): origin and destination are the same node
                ans = 1.0
            else:
                visited = set()
                ans = self.backtrack_evaluate(table,num, denum, 1, visited)
            
            results.append(ans)

        return results    
            
            
    def backtrack_evaluate(self,graph ,curr_node, target_node, acc_product, visited):
        visited.add(curr_node)
        ret = -1.0
        neighbors = graph[curr_node]
        if target_node in neighbors:
            ret = acc_product * neighbors[target_node]
        else:
            for neighbor, value in neighbors.items():
                if neighbor in visited:
                    continue
                ret = self.backtrack_evaluate(
                    graph, neighbor, target_node, acc_product * value, visited)
                if ret != -1.0:
                    break
        visited.remove(curr_node)
        return ret            


