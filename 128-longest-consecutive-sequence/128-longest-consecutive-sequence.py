class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #remove duplicates
        nums = set(nums)
        print(nums)
        d = []
        # creating a dictionary of sequence starting numbers
        for i in nums:
            #checking if the element is the start of sequence
            if i - 1 not in nums:
                d.append(i) 
        print(d)
        i = 0
        m = 0
        p = {}
        for _ in range(len(nums)):
            if i not in p: 
                p[i] = [d[i]]
            m = m + 1
            if d[i] + m in nums:
                p[i].append(d[i] + m)
            else:
                i = i + 1
                m = 0
        print(p)
        n = 0
        for i in p:
            if len(p[i]) > n:
                n = len(p[i])
        return n
                        