class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def graph(v, index, arr):
            arr.append(candidates[index])
            if v == target:
                output.append(arr.copy())
                return True
            if v > target:
                arr.pop()
                return False
            for i in range(index, len(candidates)):
                val = v + candidates[i]
                if graph(val, i, arr):
                    arr.pop()
                    val -= candidates[i]
            arr.pop()
        for ind, c in enumerate(candidates):
            array = []
            graph(c, ind, array)
        return output