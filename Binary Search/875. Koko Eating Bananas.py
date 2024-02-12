# https://leetcode.com/problems/koko-eating-bananas/description/

from typing import List
from copy import copy
import math


# Too slow, count time dont go through list

# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         piles.sort()
#         l, hi = piles[0], piles[-1]
#         min_k = piles[-1]

#         while l <= hi:
#             k = l + (hi - l)//2
#             temp_piles =  copy(piles)
#             for _ in range(h):
#                 current_p = temp_piles.pop()

#                 if current_p - k > 0:
#                     temp_piles.append(current_p - k)
                
#                 if not temp_piles:
#                     break
            
#             if not temp_piles:
#                 min_k = k if k < min_k else min_k
#                 hi = k - 1

#             elif temp_piles:
#                 l = k + 1
        
#         return min_k


from copy import copy

# copied solution, not mine
# pretty much he counts how much time will he spend on eating piles (p). 
# If total time (totalTime) with current k is smaller than givent time (h) it means it Koko will eat faster
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res



if __name__ == "__main__":
    a = Solution()
    print(a.minEatingSpeed(piles = [3,6,7,11], h = 8))
    print(a.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
    print(a.minEatingSpeed(piles = [30,11,23,4,20], h = 6))


    # 3 6 7 11