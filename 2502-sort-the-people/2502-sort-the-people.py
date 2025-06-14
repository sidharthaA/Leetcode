class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heap_heights = [(-height, i) for i, height in enumerate(heights)]
        heapq.heapify(heap_heights)
        res = []
        while heap_heights:
            _, i = heapq.heappop(heap_heights)
            res.append(names[i])
        return res