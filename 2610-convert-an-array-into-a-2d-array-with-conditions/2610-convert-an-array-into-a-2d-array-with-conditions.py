class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = {}
        result = [[]]
        for num in nums:
            if num in count:
                index = count[num]
                if len(result) - 1 < index:
                    result.append([num])
                else:
                    result[index].append(num)
                count[num] += 1
            else:
                count[num] = 1
                result[0].append(num)
        return result
        