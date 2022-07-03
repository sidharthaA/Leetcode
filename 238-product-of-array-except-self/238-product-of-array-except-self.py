class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        bucket = [1]    
        for i in nums[:-1]:
            product = product * i
            bucket.append(product)        
        nums.reverse()
        product = 1
        bucket.reverse()
        l = 1
        for i in nums[:-1]:
            product = product * i
            bucket[l] = bucket[l] * product
            l = l+ 1
        bucket.reverse()
        return bucket
        
        