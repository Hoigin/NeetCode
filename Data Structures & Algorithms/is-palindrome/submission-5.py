import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not re.match(r'^[a-zA-Z0-9]', s[r]):
                r -= 1
            while l < r and not re.match(r'^[a-zA-Z0-9]', s[l]):
                l += 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True  