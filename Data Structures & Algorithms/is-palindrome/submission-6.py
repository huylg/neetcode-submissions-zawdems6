class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        end = len(s) - 1
        while low < end:
            if not s[low].isalnum():
                low += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue

            if s[low].lower() != s[end].lower():
                return False
            low += 1
            end -= 1
        return True
