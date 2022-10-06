"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        '''recursively'''
        # output = []
        # def dfs(node):
        #     if not node: return
        #     output.append(node.val)
        #     for children in node.children:
        #         dfs(children)
        # dfs(root)
        # return output
    
        '''iteratively'''
        stack = []
        output = []
        if not root: return []
        stack.append(root)
        while stack:
            candidate = stack.pop()
            output.append(candidate.val)
            stack.extend(candidate.children[::-1])
        return output