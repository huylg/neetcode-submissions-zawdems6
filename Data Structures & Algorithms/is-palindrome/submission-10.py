class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = []

        for c in s:
            if c.isalnum():
                f.append(c.lower())

        l = len(f)

        for i in range(l):
            if f[i] != f[l-i-1]:
                return False
        return True


