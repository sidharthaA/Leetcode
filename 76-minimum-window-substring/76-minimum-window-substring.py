# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         #return false id len(s) is less than len(t)
#         if len(s) < len(t):
#             return ''
        
# #         # dictionary to count frequency of characters in s
# #         tDictionary = {}
# #         for char in t:
# #             if char not in tDictionary:
# #                 tDictionary[char] = 1
# #             else:
# #                 tDictionary[char] += 1
        
# #         #initializing pointers for slidong window with window length len(t)
# #         start = 0
# #         end = len(t) - 1
# #         sDictionary = {}
        
# #         # dictionary to count frequency of characters in s of len(t)
# #         for char in s[start:end + 1]:
# #             if char not in sDictionary:
# #                 sDictionary[char] = 1
# #             else:
# #                 sDictionary[char] += 1
# #         # checkking if t is substring of s
# #         if sDictionary == tDictionary:
        
# #         # sliding the window to check for smallest window
# #         while end < len(s):
# #             if s[]
        
#         # for i in t:
            
#         pos = 0
#         target = []
        
#         for i in s:
#             if i in t:
#                 target.append(pos)
#             pos += 1
#         op = []
#         output = []
#         tDummy = t
        
#         for i in target:
#             if s[i] in tDummy:
#                 tDummy = tDummy.replace(s[i], '', 1)
#                 op.append(i)
#         output.append(op)
#         end = target.index(op[1])
#         start = 0
#         print(s[target[end]])
#         print(target)
#         while end < len(target):
#             # end += 1
#             if s[op[0]] == s[target[end]]:
#                 print(s[target[end]])
#                 op.append(target[end])
#                 del op[0]
#                 output.append(op)
#             end += 1
#             # if s[target[end]] in tDummy:
#             #     tDummy = tDummy.replace(s[target[end]], '', 1)
#             #     op.append(target[end])
#             # end += 1
#             # if tDummy == '':
#             #     output.append(op)
#             #     op = []
#             #     tDummy = t
#             #     if len(target) > len(t):
#             #         del target[0]
#             #     else:
#             #         break
#             #     end = 0
#         print(output)
#         if not output:
#             return ""
#         minim = math.inf
#         for i in output:
#             temp = i[-1] - i[0]
#             minim = min(temp, minim)
#             if temp == minim:
#                 best = i
#         return s[best[0]:best[-1]+1]

import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #创建字典
        need = {}
        window = {}

        #对need进行初始化,找到target包含的字符和个数
        for i in t:
            need[i] = need.get(i,0) + 1

        left = right = 0 #定义左右滑动窗口
        vaild = 0 #定义记录几个字符满足要求的变量
        start = 0 #最小字符串的起始索引
        length = sys.maxsize

        while right < len(s): #判断右窗口小于source字符串长度
            c = s[right] #准备移入窗口的字符
            right += 1 #窗口右移
            if need.get(c,0): #如果该字符属于need中的
                window[c] = window.get(c,0) + 1 #则加入window
                if window[c] == need[c]: #如果值相等，意味着符合要求了，valid+1
                    vaild +=1
            #窗口右移中判断是否左缩
            while vaild == len(need): #当符合要求的字符串数量达到时开始考虑左缩
                if right - left < length:
                    start = left #赋值左窗口
                    length = right - left #更新窗口长度
                d = s[left] #准备移出窗口的字符
                left += 1 #窗口左移
                if need.get(d,0): #若need中有d
                    if need[d] == window[d]: #且二者要求的数量不一样
                        vaild -= 1 #符合要求的字符-1
                    window[d] = window.get(d,0) - 1


        if length == sys.maxsize:
            return ""
        else:
            return s[ start: start+length]
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    