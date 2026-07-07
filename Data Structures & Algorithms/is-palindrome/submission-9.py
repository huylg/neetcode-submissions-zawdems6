class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        hi = len(s) - 1

        while low <= hi:
            if not s[low].isalnum():
                low+=1
            elif not s[hi].isalnum():
                hi -= 1

            elif s[low].lower() == s[hi].lower():
                low += 1
                hi -= 1
            else:
                return False


        return True

