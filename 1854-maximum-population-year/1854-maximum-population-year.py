class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        map = {}
        for log in logs:
            for i in range(log[0], log[1]):
                if i not in map:
                    map[i] = 1
                else:
                    map[i] += 1
        myKeys = list(map.keys())
        myKeys.sort()
        sorted_dict = {i: map[i] for i in myKeys}
        return max(sorted_dict, key=sorted_dict.get)