class Solution:
    def addBinary(self, a: str, b: str) -> str:
        iter = max(len(a), len(b))
        a = a[::-1]
        b = b[::-1]
        
        ans = ""
        flag = 0
        for i in range(iter):
            
            if i < min(len(a), len(b)):
                sum = int(a[i]) % 10 + int(b[i]) % 10 + flag
            elif i >= min(len(a), len(b)) and len(a) > len(b):
                sum = int(a[i]) % 10 + flag
            elif i >= min(len(a), len(b)) and len(a) < len(b):
                sum = int(b[i]) % 10 + flag
            flag = 0
                
            if sum < 2:
                ans = ans + str(sum)
            else:
                ans = ans + str(sum % 2)
                flag = 1
            
            if i == iter - 1 and flag == 1:
                ans = ans + "1"
            
        return(ans[::-1])
        