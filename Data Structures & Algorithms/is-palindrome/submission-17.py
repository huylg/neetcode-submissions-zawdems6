class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)

        start = 0
        end = l - 1

        while start < end:
            if not s[ start ].isalnum():
                start += 1
                continue
            elif not s[ end ].isalnum():
                end -= 1
                continue
            elif s[ start ].lower() != s[ end ].lower():
                return False
            else:
                start += 1
                end -= 1



        return True



