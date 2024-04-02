class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        indices = []
        for num in nums1:
            indices.append(nums2.index(num))

        for i in indices:
            num = nums2[i]
            flag = 0
            while i < len(nums2) - 1:
                if nums2[i + 1] > num:
                    ans.append(nums2[i + 1])
                    flag = 1
                    break
                i += 1
            if not flag:
                ans.append(-1)
        return ans