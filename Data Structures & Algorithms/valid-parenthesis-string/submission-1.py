class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        left = []
        star = []
        for i in range(n):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while left and star:
            if left.pop() > star.pop():
                return False
        return not left