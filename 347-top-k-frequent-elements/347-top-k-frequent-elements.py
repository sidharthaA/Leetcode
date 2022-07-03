class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        for i in nums:
            if i in frequent:
                frequent[i] = frequent[i] + 1
            else:
                frequent[i] = 1
        output = []
        for i in range(k):
            val = list(frequent.keys())[list(frequent.values()).index(max(frequent.values()))]
            output = output + [val]
            del frequent[val]
        return output
        
    
    