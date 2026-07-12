class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}':'{',']':'[',')':'('}
        
        n = len(s)
        i = 0
        while i < n:
            if stack and s[i] in pairs:
                if stack[-1] != pairs[s[i]]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return True if not stack else False