class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #check length, if there not equal then maybe invalid

        dic_s = {}
        dic_t = {}
        #get the frequency of the words
        
        for char in s:
            if char not in dic_s:
                dic_s[char] = 1
            dic_s[char] = dic_s[char] + 1
        
        for char2 in t:
            if char2 not in dic_t:
                dic_t[char2] = 1
            dic_t[char2] = dic_t[char2] + 1
        
        print(dic_s, dic_t)
        
        
        
        return dic_s == dic_t
        

