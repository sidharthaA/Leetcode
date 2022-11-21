class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        position_nums2_original = {}
        position_nums2_sorted = {}
        # for pos, i in enumerate(nums2):
        #     position_nums2_original[pos] = i
        # nums2.sort()
        # print(position_nums2_original)
        # print(nums2)
        
        # product_sum = 0
        # for pos, i in nums1:
        #     product_sum += max(nums2) * min(nums1)
        
        product_sum = 0
        nums2.sort()
        nums1.sort()
        nums = len(nums1) - 1
        for i in range(nums + 1):
            product_sum += nums2[i] * nums1[nums - i]
        return product_sum