class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        star = 0
        end = len(s)-1

        while star < end:
            if s[star] not in "abcdefghijklmnopqrstuvwxyz1234567890":
                star += 1
                continue
            
            if s[end] not in "abcdefghijklmnopqrstuvwxyz1234567890":
                end -= 1
                continue

            if s[star] == s[end]:
                star += 1
                end -= 1
                continue
            else:
                return False


        return True 
        
        