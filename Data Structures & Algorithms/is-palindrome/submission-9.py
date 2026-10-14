class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_str = "".join(char.lower() for char in s if char.isalnum())
        
        li = list(clean_str)

        if not li:
            return True
        beg = 0
        end = len(li)-1

        print(beg, end)
    
        while beg < end:
            if li[beg] != li[end]:
                return False
            beg += 1
            end -= 1
            
        return True
        