class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        count = 0
        for i in range(len(distance)):
            if start + i < len(distance):
                if start + i == destination:
                    break
                else:
                    count += distance[start + i]
            else:
                if (start + i) % len(distance) == destination:
                    break
                else:
                    ph = (start + i) % len(distance)
                    count += distance[ph]
        
        count_rev = 0
        for i in range(len(distance)):
            if destination + i < len(distance):
                if destination + i == start:
                    break
                else:
                    count_rev += distance[destination + i]
            else:
                if (destination + i) % len(distance) == start:
                    break
                else:
                    ph = (destination + i) % len(distance)
                    count_rev += distance[ph]
        # print(count, count_rev)
        return min(count, count_rev)