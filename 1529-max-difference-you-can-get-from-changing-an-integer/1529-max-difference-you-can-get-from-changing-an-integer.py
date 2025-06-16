# class Solution:
#     def maxDiff(self, num: int) -> int:
#         s = str(num)
#         high, low = [], []
#         high_val, low_val = '', ''
#         high_flag, low_flag = False, '2'
#         for i in range(len(s)):
#             if s[i] != '9' and not high_flag:
#                 high_val = s[i]
#                 high_flag = True
#             if high_flag and s[i] == high_val:
#                 high.append('9')
#             else:
#                 high.append(s[i])
            
#             if i == 0 and s[i] != '1':
#                 low_val = s[i]
#                 low_flag = '1'
#             elif i > 0 and s[i] != '0' and low_val == '':
#                 low_val = s[i]
#                 low_flag = '0'
#             if int(low_flag) < 2 and s[i] == low_val:
#                 low.append(low_flag)
#             else:
#                 low.append(s[i])

#         val_high, val_low = int("".join(high)), int("".join(low))
        
#         print(val_high, val_low, val_high - val_low)
#         return val_high - val_low

class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        high, low = [], []
        high_val, low_val = '', ''
        high_flag = False
        low_flag = ''  # Corrected from '2' to ''

        for i in range(len(s)):
            # Build the highest possible number by replacing all occurrences of the first non-9 digit with 9
            if not high_flag and s[i] != '9':
                high_val = s[i]
                high_flag = True
            if high_flag and s[i] == high_val:
                high.append('9')
            else:
                high.append(s[i])

            # Build the lowest possible number
            if i == 0:
                if s[i] != '1':
                    low_val = s[i]
                    low_flag = '1'
                # Else, leave low_val empty for now, to catch from i > 0
            elif low_val == '' and s[i] != '0' and s[i] != '1':
                low_val = s[i]
                low_flag = '0'
            
            if low_val != '' and s[i] == low_val:
                low.append(low_flag)
            else:
                low.append(s[i])

        val_high = int("".join(high))
        val_low = int("".join(low))
        
        return val_high - val_low