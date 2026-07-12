class Solution:
    def isAlphaNumeric(self, c: str) -> bool:
        return (
            ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9')
        )
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1
            while left < right and not self.isAlphaNumeric(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
