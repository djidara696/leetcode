class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        print( sorted(s) , sorted(t))
        


if __name__ == '__main__':
    print(Solution().isAnagram("rat", "car"))