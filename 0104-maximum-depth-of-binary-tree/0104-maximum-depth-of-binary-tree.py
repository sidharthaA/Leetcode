# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        q = deque()
        q.append(root)
        while q and root:
            count += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # if not root:
        # #     return 0
        # # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # if not root:
        #     return 0
        
        # q = collections.deque()
        # q.append(root)
        # level = 0
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
            
        #     level += 1
        # return level
                
