'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        
        maxSum = float('-inf')
        
        def dfs(node):
            nonlocal maxSum
            if not node:
                return float('-inf')
            left = dfs(node.left)
            right = dfs(node.right)
            
            curMax = max(left+node.data, right+node.data, node.data)
            maxSum = max(maxSum, curMax, left, right, left+right+node.data)
            
            # print(curMax)
            # print(maxSum)
            # print(' ')
            return curMax
            
        dfs(root)
            
        return maxSum