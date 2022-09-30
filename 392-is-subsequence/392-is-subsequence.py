class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # dictionary to track the positions of each character
        count_dictionary = {}
        for index, character in enumerate(t):
            if character in count_dictionary:
                count_dictionary[character].append(index)
            else: 
                count_dictionary[character] = [index]
        print(count_dictionary)
            
        # Check each character in the dictionary if the position values are incrementing
        current = float('-inf') # to keep a track of current position
        flag = True
        for character in s:
            if character not in count_dictionary:
                return False
            for position in count_dictionary[character]:
                if position > current:
                    current = position
                    flag = False
                    break
            if flag == True:
                return False
            flag = True
        return True
            
            