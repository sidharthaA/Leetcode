# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # output = []
        def binary_search(nums):
            if nums:
                mid = len(nums) // 2
                print(mid)
                newtree = TreeNode(nums[mid])
                newtree.left = binary_search(nums[:mid])
                newtree.right = binary_search(nums[mid + 1:])
                
                return newtree
            
        
        return binary_search(nums)