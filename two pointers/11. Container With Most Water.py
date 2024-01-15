from typing import List
import math

# too slow
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         def calc_min_d(max_volume, i):
#             return len(height) if height[i] == 0 else math.ceil((max_volume + 1) / height[i])
        
#         i, j = 0, len(height) - 1
#         max_volume = 0
#         min_d = 0


#         while i < j:
#             m_h = min(height[i], height[j])
#             d = j - i

#             temp_volume = m_h * d
#             if temp_volume >= max_volume:
#                 max_volume = temp_volume

#                 min_d = calc_min_d(max_volume, i)
            
#             j -= 1
            
#             while (j - i) < min_d and i < len(height) - 1:
#                 i += 1
#                 j = len(height) - 1
#                 min_d = calc_min_d(max_volume, i)
        
#         return max_volume


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_volume = 0

        while i < j:
            max_volume = max(max_volume, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_volume

if __name__ == "__main__":
    a = Solution()
    print(a.maxArea(height = [1,8,6,2,5,4,8,3,7]))
    print(a.maxArea(height = [2, 0]))
    print(a.maxArea(height = [1,0,0,0,0,0,0,2,2]))
    print(a.maxArea(height = [0,14,6,2,10,9,4,1,10,3]))