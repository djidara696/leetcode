import re
import math


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^A-Za-z0-9]+', '', s)

        for i in range(math.ceil(len(s)/2)):
            if s[i] != s[-1 - i]:
                return False
            
        return True

a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))
print(a.isPalindrome("race a car"))
print(a.isPalindrome(" "))