import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if not re.match(r'^[a-zA-Z0-9]', s[r]):
                r -= 1
                continue
            if not re.match(r'^[a-zA-Z0-9]', s[l]):
                l += 1
                continue
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True  