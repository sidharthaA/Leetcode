class Solution:
    def minMaxDifference(self, num: int) -> int:
        change_max = []
        change = ''
        final_max = []
        flag = True
        small = str(num)[0]
        final_min = []
        for i, n in enumerate(str(num)):
            if n != '9' and flag:
                change = n
                flag = False
            if n == change:
                
                change_max.append(i)
                final_max.append('9')
            else:
                final_max.append(n)
            if n == small:
                final_min.append('0')
            else:
                final_min.append(n)
        
        max_val = int("".join(final_max))
        min_val = int("".join(final_min))
        return max_val - min_val