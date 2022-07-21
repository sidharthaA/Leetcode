class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def graph(v, index, arr):
            # print("#########output#########", output)
            arr.append(candidates[index])
            # print(arr, index, candidates[index], v)
            if v == target:
                output.append(arr.copy())
                # print(output)
                # print(111111111111111)
                return True
            if v > target:
                arr.pop()
                # print(222222222222222, arr)
                return False
            for i in range(index, len(candidates)):
                val = v + candidates[i]
                if graph(val, i, arr):
                    # print("inside true",arr)
                    arr.pop()
                    val -= candidates[i]
                    # print(val)
            arr.pop()

        # candidates = [2,3,6,7]
        # target = 7
        # global count
        # count = 0
        for ind, c in enumerate(candidates):
            array = []
            # print("new", ind, c)
            graph(c, ind, array)
        return output
