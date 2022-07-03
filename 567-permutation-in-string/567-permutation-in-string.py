class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # print("next testcase:")
        # Check if s1 is a substring of s2
        if len(s2) < len(s1):
            return False
        
        d, e = {}, {}
        
        # Create a hashmap to store the letter frequency of s1
        for i in s1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        # print("s1:", d)
        
        # Pointers to create a window of len(s1)
        start = 0
        end = len(s1) -1
        # print(s2[:end+1])
        
        # Create a hashmap to store the first len(s1) letter frequency of s2
        for i in s2[start:end + 1]:
            if i not in e:
                e[i] = 1
            else:
                e[i] += 1
        # print("initial window:", e)
        print(e)
                
        # Return True if dictionaries of len(s1) of both s1 and s2 are equal
        if d == e:
            return True
        
        # Implementing sliding window to check for s1 permutations in s2
        while end < len(s2) - 1:
            end += 1
            start += 1
            # print("before changes window:", e)
            # Moving the window by 1 char and dealing with (start - 1)'th character
            if s2[end] not in e:
                e[s2[end]] = 1
                
            else:
                e[s2[end]] += 1
            # print(" changes :", e)  
            # Decrement the frequency of (start - 1)'th character if it's in s1 by 1
            if e[s2[start - 1]] == 1:
                    del e[s2[start - 1]]
            else:
                e[s2[start - 1]] -= 1
            # print("after changes window:", e)
            
            # Return True if dictionaries of len(s1) of both s1 and s2 are equal
            if d == e:
                return True
            
        return False