class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(','}':'{',']':'['}

        for char in s:
            if not stack or char not in pairs:
                stack.append(char)
            else:
                if stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop()
        return True if not stack else False

