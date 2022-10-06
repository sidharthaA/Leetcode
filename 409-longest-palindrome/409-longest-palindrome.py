class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for character in s:
            if character not in count:
                count[character] = 1
            else:
                count[character] += 1
        longest = 0
        flag = True
        # if 1 in count.values():
        #     longest += 1
        #     flag = False
        for value in count.values():
            if value == 1 and flag:
                longest += 1
                flag = False
                print(longest)
            if flag and value % 2 != 0:
                longest += 1
                flag = False
                print(longest)
            if value // 2 >= 1:
                longest += (value // 2) * 2
                print(longest)
        return longest