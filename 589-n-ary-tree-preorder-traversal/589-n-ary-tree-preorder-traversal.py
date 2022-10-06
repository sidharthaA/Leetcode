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
        stack = deque()
        output = []
        if not root: return
        stack.appendleft(root)
        while stack:
            candidate = stack.popleft()
            output.append(candidate.val)
            for child in reversed(candidate.children):
                stack.appendleft(child)
        return output
        