class Solution:
    def myAtoi(self, s: str) -> int:
        # nums = {'0' : 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '-': 10, '+': 11}
        # mul = 1
        # ans = 0
        # flag = False
        # for c in s[::-1]:
        #     if c not in nums:
        #         continue
        #     if c == '-':
        #         flag = True
        #     if c in nums and c not in '+-':
        #         ans += nums[c] * mul
        #         mul *= 10
        # if flag:
        #     ans *= -1
        # if ans in range(pow(-2, 31), pow(2, 31)):
        #     return ans
        # else:
        #     if flag:
        #         return pow(-2, 31)
        #     else:
        #         return pow(2, 31)
        
        
        res=s.strip()
        if not res:
            return 0
        i=0
        sign=1
        if res[i]=='+':
                 i+=1
        elif res[i]=='-':
                 i+=1
                 sign=-1

        parsed=0

        while i<len(res):
            curr=res[i]

            if not curr.isdigit():
                break
            else:
                parsed=parsed*10+int(curr)
            i+=1
            print(parsed)
        parsed*=sign





        if parsed<-2**31:

            return -2**31

        elif parsed>(2**31)-1:

            return (2**31)-1
        else:
            return parsed
                