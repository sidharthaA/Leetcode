class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        i, j = 0, 1
        result = 0
        while j < len(bank) and i < j:
            count_i, count_j = 0, 0
            for num in bank[i]:
                if num == "1":
                    count_i += 1
            for num in bank[j]:
                if num == "1":
                    count_j += 1
            # print(count_i, count_j)
            if count_i > 0 and count_j > 0:
                print(1)
                result += count_i * count_j
                i = j
                j += 1
            elif count_i == 0 and count_j == 0:
                print(2)
                i += 2
                j += 2
            elif count_i == 0:
                i += 1
                if i >= j:
                    j = i + 1
            elif count_j == 0:
                j += 1
        return result

            