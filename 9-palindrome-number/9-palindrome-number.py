class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_reverse = 0
        x_duplicate = x
        if x < 0:
            return False
        if x < 10:
            return True      
        while x != 0:
            x_reverse = x_reverse * 10 + x % 10
            x = x // 10
        if x_reverse == x_duplicate:
            return True
        else: 
            return False